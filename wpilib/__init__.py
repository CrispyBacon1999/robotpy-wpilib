from . import _init_wpilib

# autogenerated by 'robotpy-build create-imports wpilib wpilib._wpilib'
from ._wpilib import (
    ADXL345_I2C,
    ADXL345_SPI,
    ADXL362,
    ADXRS450_Gyro,
    AnalogAccelerometer,
    AnalogEncoder,
    AnalogGyro,
    AnalogInput,
    AnalogOutput,
    AnalogPotentiometer,
    AnalogTrigger,
    AnalogTriggerOutput,
    AnalogTriggerType,
    BuiltInAccelerometer,
    CAN,
    CANData,
    CANStatus,
    Color,
    Color8Bit,
    Compressor,
    Counter,
    DMC60,
    DigitalGlitchFilter,
    DigitalInput,
    DigitalOutput,
    DigitalSource,
    DoubleSolenoid,
    DriverStation,
    DutyCycle,
    DutyCycleEncoder,
    Encoder,
    Error,
    ErrorBase,
    GyroBase,
    InterruptableSensorBase,
    IterativeRobot,
    IterativeRobotBase,
    Jaguar,
    Joystick,
    LiveWindow,
    MotorSafety,
    NidecBrushless,
    Notifier,
    PIDController,
    PWM,
    PWMSparkMax,
    PWMSpeedController,
    PWMTalonFX,
    PWMTalonSRX,
    PWMVenom,
    PWMVictorSPX,
    PowerDistributionPanel,
    Preferences,
    RamseteController,
    Relay,
    RobotBase,
    RobotController,
    RobotState,
    SD540,
    Sendable,
    SendableBase,
    SendableBuilder,
    SendableBuilderImpl,
    SendableRegistry,
    SensorUtil,
    SerialPort,
    Servo,
    SmartDashboard,
    Solenoid,
    SolenoidBase,
    Spark,
    SpeedControllerGroup,
    Talon,
    TimedRobot,
    Timer,
    Ultrasonic,
    Victor,
    VictorSP,
    Watchdog,
    XboxController,
    getCurrentThreadPriority,
    getDeployDirectory,
    getLaunchDirectory,
    getOperatingDirectory,
    getThreadPriority,
    getTime,
    setCurrentThreadPriority,
    setThreadPriority,
    wait,
    wpi_error_s_AnalogTriggerLimitOrderError,
    wpi_error_s_AnalogTriggerPulseOutputError,
    wpi_error_s_BadJoystickAxis,
    wpi_error_s_BadJoystickIndex,
    wpi_error_s_CameraServerError,
    wpi_error_s_ChannelIndexOutOfRange,
    wpi_error_s_CommandIllegalUse,
    wpi_error_s_CompassManufacturerError,
    wpi_error_s_CompassTypeError,
    wpi_error_s_CompressorAlreadyDefined,
    wpi_error_s_CompressorNonMatching,
    wpi_error_s_CompressorTaskError,
    wpi_error_s_CompressorUndefined,
    wpi_error_s_DashboardDataCollision,
    wpi_error_s_DashboardDataOverflow,
    wpi_error_s_DriveUninitialized,
    wpi_error_s_DriverStationTaskError,
    wpi_error_s_EnhancedIOMissing,
    wpi_error_s_EnhancedIOPWMPeriodOutOfRange,
    wpi_error_s_IncompatibleMode,
    wpi_error_s_IncompatibleState,
    wpi_error_s_InconsistentArrayValueAdded,
    wpi_error_s_IncorrectBatteryChannel,
    wpi_error_s_InvalidMotorIndex,
    wpi_error_s_InvalidParameter,
    wpi_error_s_JaguarMessageNotFound,
    wpi_error_s_JaguarVersionError,
    wpi_error_s_LineNotOutput,
    wpi_error_s_LoopTimingError,
    wpi_error_s_MismatchedComplexTypeClose,
    wpi_error_s_ModuleIndexOutOfRange,
    wpi_error_s_NetworkTablesBufferFull,
    wpi_error_s_NetworkTablesCorrupt,
    wpi_error_s_NetworkTablesReadError,
    wpi_error_s_NetworkTablesWrongType,
    wpi_error_s_NoAvailableResources,
    wpi_error_s_NonBinaryDigitalValue,
    wpi_error_s_NotAllocated,
    wpi_error_s_NullParameter,
    wpi_error_s_ParameterOutOfRange,
    wpi_error_s_ResourceAlreadyAllocated,
    wpi_error_s_SPIClockRateTooLow,
    wpi_error_s_SPIReadNoData,
    wpi_error_s_SPIReadNoMISO,
    wpi_error_s_SPIWriteNoMOSI,
    wpi_error_s_SampleRateTooHigh,
    wpi_error_s_SmartDashboardMissingKey,
    wpi_error_s_TaskDeletedError,
    wpi_error_s_TaskError,
    wpi_error_s_TaskIDError,
    wpi_error_s_TaskMemoryError,
    wpi_error_s_TaskOptionsError,
    wpi_error_s_TaskPriorityError,
    wpi_error_s_Timeout,
    wpi_error_s_UnsupportedInSimulation,
    wpi_error_s_VoltageOutOfRange,
    wpi_error_value_AnalogTriggerLimitOrderError,
    wpi_error_value_AnalogTriggerPulseOutputError,
    wpi_error_value_BadJoystickAxis,
    wpi_error_value_BadJoystickIndex,
    wpi_error_value_CameraServerError,
    wpi_error_value_ChannelIndexOutOfRange,
    wpi_error_value_CommandIllegalUse,
    wpi_error_value_CompassManufacturerError,
    wpi_error_value_CompassTypeError,
    wpi_error_value_CompressorAlreadyDefined,
    wpi_error_value_CompressorNonMatching,
    wpi_error_value_CompressorTaskError,
    wpi_error_value_CompressorUndefined,
    wpi_error_value_DashboardDataCollision,
    wpi_error_value_DashboardDataOverflow,
    wpi_error_value_DriveUninitialized,
    wpi_error_value_DriverStationTaskError,
    wpi_error_value_EnhancedIOMissing,
    wpi_error_value_EnhancedIOPWMPeriodOutOfRange,
    wpi_error_value_IncompatibleMode,
    wpi_error_value_IncompatibleState,
    wpi_error_value_InconsistentArrayValueAdded,
    wpi_error_value_IncorrectBatteryChannel,
    wpi_error_value_InvalidMotorIndex,
    wpi_error_value_InvalidParameter,
    wpi_error_value_JaguarMessageNotFound,
    wpi_error_value_JaguarVersionError,
    wpi_error_value_LineNotOutput,
    wpi_error_value_LoopTimingError,
    wpi_error_value_MismatchedComplexTypeClose,
    wpi_error_value_ModuleIndexOutOfRange,
    wpi_error_value_NetworkTablesBufferFull,
    wpi_error_value_NetworkTablesCorrupt,
    wpi_error_value_NetworkTablesReadError,
    wpi_error_value_NetworkTablesWrongType,
    wpi_error_value_NoAvailableResources,
    wpi_error_value_NonBinaryDigitalValue,
    wpi_error_value_NotAllocated,
    wpi_error_value_NullParameter,
    wpi_error_value_ParameterOutOfRange,
    wpi_error_value_ResourceAlreadyAllocated,
    wpi_error_value_SPIClockRateTooLow,
    wpi_error_value_SPIReadNoData,
    wpi_error_value_SPIReadNoMISO,
    wpi_error_value_SPIWriteNoMOSI,
    wpi_error_value_SampleRateTooHigh,
    wpi_error_value_SmartDashboardMissingKey,
    wpi_error_value_TaskDeletedError,
    wpi_error_value_TaskError,
    wpi_error_value_TaskIDError,
    wpi_error_value_TaskMemoryError,
    wpi_error_value_TaskOptionsError,
    wpi_error_value_TaskPriorityError,
    wpi_error_value_Timeout,
    wpi_error_value_UnsupportedInSimulation,
    wpi_error_value_VoltageOutOfRange,
)

__all__ = [
    "ADXL345_I2C",
    "ADXL345_SPI",
    "ADXL362",
    "ADXRS450_Gyro",
    "AnalogAccelerometer",
    "AnalogEncoder",
    "AnalogGyro",
    "AnalogInput",
    "AnalogOutput",
    "AnalogPotentiometer",
    "AnalogTrigger",
    "AnalogTriggerOutput",
    "AnalogTriggerType",
    "BuiltInAccelerometer",
    "CAN",
    "CANData",
    "CANStatus",
    "Color",
    "Color8Bit",
    "Compressor",
    "Counter",
    "DMC60",
    "DigitalGlitchFilter",
    "DigitalInput",
    "DigitalOutput",
    "DigitalSource",
    "DoubleSolenoid",
    "DriverStation",
    "DutyCycle",
    "DutyCycleEncoder",
    "Encoder",
    "Error",
    "ErrorBase",
    "GyroBase",
    "InterruptableSensorBase",
    "IterativeRobot",
    "IterativeRobotBase",
    "Jaguar",
    "Joystick",
    "LiveWindow",
    "MotorSafety",
    "NidecBrushless",
    "Notifier",
    "PIDController",
    "PWM",
    "PWMSparkMax",
    "PWMSpeedController",
    "PWMTalonFX",
    "PWMTalonSRX",
    "PWMVenom",
    "PWMVictorSPX",
    "PowerDistributionPanel",
    "Preferences",
    "RamseteController",
    "Relay",
    "RobotBase",
    "RobotController",
    "RobotState",
    "SD540",
    "Sendable",
    "SendableBase",
    "SendableBuilder",
    "SendableBuilderImpl",
    "SendableRegistry",
    "SensorUtil",
    "SerialPort",
    "Servo",
    "SmartDashboard",
    "Solenoid",
    "SolenoidBase",
    "Spark",
    "SpeedControllerGroup",
    "Talon",
    "TimedRobot",
    "Timer",
    "Ultrasonic",
    "Victor",
    "VictorSP",
    "Watchdog",
    "XboxController",
    "getCurrentThreadPriority",
    "getDeployDirectory",
    "getLaunchDirectory",
    "getOperatingDirectory",
    "getThreadPriority",
    "getTime",
    "setCurrentThreadPriority",
    "setThreadPriority",
    "wait",
    "wpi_error_s_AnalogTriggerLimitOrderError",
    "wpi_error_s_AnalogTriggerPulseOutputError",
    "wpi_error_s_BadJoystickAxis",
    "wpi_error_s_BadJoystickIndex",
    "wpi_error_s_CameraServerError",
    "wpi_error_s_ChannelIndexOutOfRange",
    "wpi_error_s_CommandIllegalUse",
    "wpi_error_s_CompassManufacturerError",
    "wpi_error_s_CompassTypeError",
    "wpi_error_s_CompressorAlreadyDefined",
    "wpi_error_s_CompressorNonMatching",
    "wpi_error_s_CompressorTaskError",
    "wpi_error_s_CompressorUndefined",
    "wpi_error_s_DashboardDataCollision",
    "wpi_error_s_DashboardDataOverflow",
    "wpi_error_s_DriveUninitialized",
    "wpi_error_s_DriverStationTaskError",
    "wpi_error_s_EnhancedIOMissing",
    "wpi_error_s_EnhancedIOPWMPeriodOutOfRange",
    "wpi_error_s_IncompatibleMode",
    "wpi_error_s_IncompatibleState",
    "wpi_error_s_InconsistentArrayValueAdded",
    "wpi_error_s_IncorrectBatteryChannel",
    "wpi_error_s_InvalidMotorIndex",
    "wpi_error_s_InvalidParameter",
    "wpi_error_s_JaguarMessageNotFound",
    "wpi_error_s_JaguarVersionError",
    "wpi_error_s_LineNotOutput",
    "wpi_error_s_LoopTimingError",
    "wpi_error_s_MismatchedComplexTypeClose",
    "wpi_error_s_ModuleIndexOutOfRange",
    "wpi_error_s_NetworkTablesBufferFull",
    "wpi_error_s_NetworkTablesCorrupt",
    "wpi_error_s_NetworkTablesReadError",
    "wpi_error_s_NetworkTablesWrongType",
    "wpi_error_s_NoAvailableResources",
    "wpi_error_s_NonBinaryDigitalValue",
    "wpi_error_s_NotAllocated",
    "wpi_error_s_NullParameter",
    "wpi_error_s_ParameterOutOfRange",
    "wpi_error_s_ResourceAlreadyAllocated",
    "wpi_error_s_SPIClockRateTooLow",
    "wpi_error_s_SPIReadNoData",
    "wpi_error_s_SPIReadNoMISO",
    "wpi_error_s_SPIWriteNoMOSI",
    "wpi_error_s_SampleRateTooHigh",
    "wpi_error_s_SmartDashboardMissingKey",
    "wpi_error_s_TaskDeletedError",
    "wpi_error_s_TaskError",
    "wpi_error_s_TaskIDError",
    "wpi_error_s_TaskMemoryError",
    "wpi_error_s_TaskOptionsError",
    "wpi_error_s_TaskPriorityError",
    "wpi_error_s_Timeout",
    "wpi_error_s_UnsupportedInSimulation",
    "wpi_error_s_VoltageOutOfRange",
    "wpi_error_value_AnalogTriggerLimitOrderError",
    "wpi_error_value_AnalogTriggerPulseOutputError",
    "wpi_error_value_BadJoystickAxis",
    "wpi_error_value_BadJoystickIndex",
    "wpi_error_value_CameraServerError",
    "wpi_error_value_ChannelIndexOutOfRange",
    "wpi_error_value_CommandIllegalUse",
    "wpi_error_value_CompassManufacturerError",
    "wpi_error_value_CompassTypeError",
    "wpi_error_value_CompressorAlreadyDefined",
    "wpi_error_value_CompressorNonMatching",
    "wpi_error_value_CompressorTaskError",
    "wpi_error_value_CompressorUndefined",
    "wpi_error_value_DashboardDataCollision",
    "wpi_error_value_DashboardDataOverflow",
    "wpi_error_value_DriveUninitialized",
    "wpi_error_value_DriverStationTaskError",
    "wpi_error_value_EnhancedIOMissing",
    "wpi_error_value_EnhancedIOPWMPeriodOutOfRange",
    "wpi_error_value_IncompatibleMode",
    "wpi_error_value_IncompatibleState",
    "wpi_error_value_InconsistentArrayValueAdded",
    "wpi_error_value_IncorrectBatteryChannel",
    "wpi_error_value_InvalidMotorIndex",
    "wpi_error_value_InvalidParameter",
    "wpi_error_value_JaguarMessageNotFound",
    "wpi_error_value_JaguarVersionError",
    "wpi_error_value_LineNotOutput",
    "wpi_error_value_LoopTimingError",
    "wpi_error_value_MismatchedComplexTypeClose",
    "wpi_error_value_ModuleIndexOutOfRange",
    "wpi_error_value_NetworkTablesBufferFull",
    "wpi_error_value_NetworkTablesCorrupt",
    "wpi_error_value_NetworkTablesReadError",
    "wpi_error_value_NetworkTablesWrongType",
    "wpi_error_value_NoAvailableResources",
    "wpi_error_value_NonBinaryDigitalValue",
    "wpi_error_value_NotAllocated",
    "wpi_error_value_NullParameter",
    "wpi_error_value_ParameterOutOfRange",
    "wpi_error_value_ResourceAlreadyAllocated",
    "wpi_error_value_SPIClockRateTooLow",
    "wpi_error_value_SPIReadNoData",
    "wpi_error_value_SPIReadNoMISO",
    "wpi_error_value_SPIWriteNoMOSI",
    "wpi_error_value_SampleRateTooHigh",
    "wpi_error_value_SmartDashboardMissingKey",
    "wpi_error_value_TaskDeletedError",
    "wpi_error_value_TaskError",
    "wpi_error_value_TaskIDError",
    "wpi_error_value_TaskMemoryError",
    "wpi_error_value_TaskOptionsError",
    "wpi_error_value_TaskPriorityError",
    "wpi_error_value_Timeout",
    "wpi_error_value_UnsupportedInSimulation",
    "wpi_error_value_VoltageOutOfRange",
]

del _init_wpilib

try:
    from .version import version as __version__
except ImportError:
    __version__ = "master"

from ._impl.main import run
