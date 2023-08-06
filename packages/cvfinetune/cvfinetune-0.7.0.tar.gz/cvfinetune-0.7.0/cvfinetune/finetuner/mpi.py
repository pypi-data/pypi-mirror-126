import chainermn
import logging
import warnings

from chainermn import scatter_dataset as scatter

from cvfinetune.finetuner.base import DefaultFinetuner

class MPIFinetuner(DefaultFinetuner):

	def __init__(self, *args, comm, **kwargs):
		self.comm = comm
		super(MPIFinetuner, self).__init__(*args, **kwargs)

	@property
	def mpi(self):
		return self.comm is not None

	@property
	def mpi_main_process(self):
		return not (self.comm is not None and self.comm.rank != 0)

	def gpu_config(self, devices):

		if not self.mpi:
			msg = "Using MPIFinetuner without setting a communicator!"
			warnings.warn(msg)
			logging.warn(msg)
			return super(MPIFinetuner, self).gpu_config(devices)

		if len(devices) > 1:
			self.device_id = devices[self.comm.rank]
		else:
			self.device_id += self.comm.intra_rank

		device = self.init_device()
		ranks = f"{self.comm.rank} | {self.comm.intra_rank} | {self.comm.inter_rank}"
		logging.info(f"Node with ranks {ranks} assigned to {device}")
		return device


	def scatter_datasets(self):
		if self.mpi:
			self.train_data = scatter(self.train_data, self.comm)
			self.val_data = scatter(self.val_data, self.comm)
		else:
			logging.warn("Data scattering was not Possible!")


	def init_datasets(self, *args, **kwargs):

		if self.mpi_main_process:
			super(MPIFinetuner, self).init_datasets(*args, **kwargs)
		else:
			self.train_data, self.val_data = None, None

		self.scatter_datasets()

	def init_optimizer(self, opts):
		super(MPIFinetuner, self).init_optimizer(opts)

		if self.mpi:
			self.opt = chainermn.create_multi_node_optimizer(self.opt, self.comm)

	def init_evaluator(self):
		super(MPIFinetuner, self).init_evaluator()

		if self.mpi:
			self.evaluator = chainermn.create_multi_node_evaluator(
				self.evaluator, self.comm)

	def run(self, trainer_cls, opts, *args, **kwargs):
		if not self.mpi_main_process:
			kwargs["no_observe"] = True
			opts.no_snapshot = True
			opts.no_progress = True
			self.evaluator._progress_bar = False

		super(MPIFinetuner, self).run(trainer_cls, opts, *args, **kwargs)
