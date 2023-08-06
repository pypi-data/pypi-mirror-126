from ..Internal import Instrument
from typing import Tuple
from ..Internal import Conversions


class Utilities:
	"""Common utility class.
	Utility functions common for all types of drivers."""
	def __init__(self, io: Instrument, driver_version: str):
		self._io = io
		self._driver_version = driver_version

	@property
	def driver_version(self) -> str:
		"""Returns the instrument driver version."""
		return self._driver_version

	@property
	def idn_string(self) -> str:
		"""SCPI Command: *IDN?
		Returns instrument's Identification string."""
		return self._io.idn_string

	@property
	def manufacturer(self) -> str:
		"""Returns manufacturer of the instrument."""
		return self._io.manufacturer

	@property
	def instrument_model_full_name(self) -> str:
		"""Returns the current instrument's full name e.g. 'FSW26'."""
		return self._io.full_model_name

	@property
	def instrument_model_name(self) -> str:
		"""Returns the current instrument's family name e.g. 'FSW'."""
		return self._io.model

	@property
	def instrument_firmware_version(self) -> str:
		"""Returns instrument's firmware version."""
		return self._io.firmware_version

	@property
	def instrument_serial_number(self) -> str:
		"""Returns instrument's serial_number."""
		return self._io.serial_number

	def preset(self) -> None:
		"""SCPI command: SYST:PRES \n
		Presets the instrument to the default settings:
		Outer:
		Velocity [°/s]: 70
		Acceleration [°/s2] 2000
		Deceleration [°/s2] 2000
		Jerk [°/s3] 5000
		Custom offset [°] 0

		Inner:
		Velocity [°/s]: 15
		Acceleration [°/s2] 1500
		Deceleration [°/s2] 1500
		Jerk [°/s3] 2250
		Custom offset [°] 0
		"""
		return self._io.preset()

	def get_current_status(self) -> Tuple:
		"""SCPI command: SYST:STAT? \n
		Queries the Outer and Inner positions and movement status all in one command.
		Returns Tuple of: outer_pos, outer_movement, inner_pos, inner_movement"""
		response = self.query_str('SYST:STAT?')
		data = Conversions.str_to_str_list(response)
		outer_pos = Conversions.str_to_float(data[1])
		outer_mov = Conversions.str_to_bool(data[2])
		inner_pos = Conversions.str_to_float(data[4])
		inner_mov = Conversions.str_to_bool(data[5])
		return outer_pos, outer_mov, inner_pos, inner_mov

	@property
	def visa_timeout(self) -> int:
		"""See the visa_timeout.setter."""
		return self._io.visa_timeout

	@visa_timeout.setter
	def visa_timeout(self, value) -> None:
		"""Sets / Gets visa IO timeout in milliseconds."""
		self._io.visa_timeout = value

	@property
	def visa_manufacturer(self) -> int:
		"""Returns the manufacturer of the current VISA session."""
		return self._io.visa_manufacturer

	def write_str(self, cmd: str) -> None:
		"""Writes the command to the instrument."""
		self._io.write(cmd)

	def query_str(self, query: str) -> str:
		"""Sends the query to the instrument and returns the response as string.
		The response is trimmed of any trailing LF characters and has no length limit."""
		return self._io.query_str(query)

	def query_bool(self, query: str) -> bool:
		"""Sends the query to the instrument and returns the response as boolean."""
		return self._io.query_bool(query)

	def query_int(self, query: str) -> int:
		"""Sends the query to the instrument and returns the response as integer."""
		return self._io.query_int(query)

	def query_float(self, query: str) -> float:
		"""Sends the query to the instrument and returns the response as float."""
		return self._io.query_float(query)

	def wait_for_movements_finish(self) -> None:
		"""SYST:STAT? \n
		Waits until both the Outer and Inner movement activities stop."""
		moving = True
		while moving:
			status = self.get_current_status()
			moving = status[1] or status[3]
