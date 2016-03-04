import smbus
import struct
DEFAULT_I2C_ADDRESS = 0x1c
DEFAULT_I2C_BUS = 1

# register addresses
SYSMOD = 0x0B
XYZ_DATA_CFG = 0x0E
CTRL_REG1 = 0x2A


class MMA8452Q(object):
    """MMA8452Q Accelerometer."""
    def __init__(self, address=DEFAULT_I2C_ADDRESS, bus_num=DEFAULT_I2C_BUS):
        self.i2c_address = address
        self.i2c_bus = smbus.SMBus(bus_num)
        self.g_mul = 0  # G-force multiplier (to get G-force from interval)

    def init(self):
        """Initalises the accelerometer."""
        # Sleep rate 50 Hz, Data rate 800 Hz,
        # No reduced noise mode, Normal read mode, Active
        config = 0x3
        self.i2c_bus.write_byte_data(self.i2c_address, CTRL_REG1, config)

        # Setup range
        # register = 0x0E             # XYZ_DATA_CFG
        # data = 0x00                 # Range 2G, no high pass filtering
        xyz_config = 0x00
        self.i2c_bus.write_byte_data(self.i2c_address,
                                     XYZ_DATA_CFG,
                                     xyz_config)
        self.g_mul = 2.0 / 128       # 2G over 128 counts

        # System state
        # register = 0x0B             # SYSMOD
        sysmod_config = 0x01                 # Awake mode
        self.i2c_bus.write_byte_data(self.i2c_address, SYSMOD, sysmod_config)

        # Reset ready for reading
        self.i2c_bus.write_byte(self.i2c_address, 0x00)

    def get_xyz(self):
        status, x, y, z = self.i2c_bus.read_i2c_block_data(self.i2c_address,
                                                           0,
                                                           4)
        # convert from unsigned to signed values
        bytes = struct.pack('BBB', x, y, z)
        x, y, z = struct.unpack('bbb', bytes)
        # conver to g-force
        return x *self.g_mul, y * self.g_mul, z * self.g_mul


x = MMA8452Q()

x.init()

print(x.get_xyz())
