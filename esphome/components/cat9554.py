import voluptuous as vol

from esphome import pins
import esphome.config_validation as cv
from esphome.const import CONF_ADDRESS, CONF_ID, CONF_CAT9554
from esphome.cpp_generator import Pvariable
from esphome.cpp_helpers import setup_component
from esphome.cpp_types import App, GPIOInputPin, GPIOOutputPin, io_ns

DEPENDENCIES = ['i2c']
MULTI_CONF = True

CAT9554GPIOMode = io_ns.enum('CAT9554GPIOMode')
CAT9554_GPIO_MODES = {
    'INPUT': CAT9554GPIOMode.CAT9554_INPUT,
    'OUTPUT': CAT9554GPIOMode.CAT9554_OUTPUT,
}

CAT9554GPIOInputPin = io_ns.class_('CAT9554GPIOInputPin', GPIOInputPin)
CAT9554GPIOOutputPin = io_ns.class_('CAT9554GPIOOutputPin', GPIOOutputPin)

CONFIG_SCHEMA = cv.Schema({
    vol.Required(CONF_ID): cv.declare_variable_id(pins.CAT9554Component),
    vol.Optional(CONF_ADDRESS, default=0x20): cv.i2c_address,
}).extend(cv.COMPONENT_SCHEMA.schema)


def to_code(config):
    rhs = App.make_cat9554_component(config[CONF_ADDRESS])
    var = Pvariable(config[CONF_ID], rhs)
    setup_component(var, config)


BUILD_FLAGS = '-DUSE_CAT9554'
