import psutil
import os


#-------- Uso de los dispositivos en porcentaje ----------------
class Usage:
    def get_cpu_usage(self):
        return psutil.cpu_percent(interval=1)

    def get_ram_usage(self):
        return psutil.virtual_memory().percent

#--------- Monitor de temperatura, voltaje, carga, etc ------------------
class Monitor:
    OHM_hwtypes = [ 'Mainboard', 'SuperIO', 'CPU', 'RAM', 'GpuNvidia', 'GpuAti', 'TBalancer', 'Heatmaster', 'HDD' ]
    OHM_sensortypes = ['Voltage', 'Clock', 'Temperature', 'Load', 'Fan', 'Flow', 'Control', 'Level', 'Factor', 'Power', 'Data', 'SmallData']

    def init_OHM(self) :
        import clr 
        clr.AddReference( os.path.abspath( os.path.dirname( __file__ ) ) + R'\Drivers\OpenHardwareMonitorLib.dll' )
        from OpenHardwareMonitor import Hardware
        hw = Hardware.Computer()
        hw.MainboardEnabled, hw.CPUEnabled, hw.RAMEnabled, hw.GPUEnabled, hw.HDDEnabled = True, True, True, True, True
        hw.Open()
        return hw


    def fetch_data(self,handle) :
        
        out = []
        for i in handle.Hardware :
            i.Update()
            for sensor in i.Sensors : 
                thing = self.parse_sensor(sensor)
                if thing is not None :
                    out.append( thing )
            for j in i.SubHardware :
                j.Update()
                for subsensor in j.Sensors :
                    thing = self.parse_sensor(subsensor)
                    out.append( thing )
        return out

#------------- Acceso al sensor de temperatura de todos los dispositivos soportados--------------------
    
    def parse_sensor(self,snsr) :
 
        if snsr.Value is not None :
            if snsr.SensorType == self.OHM_sensortypes.index( 'Temperature' ) :
                HwType = self.OHM_hwtypes[ snsr.Hardware.HardwareType ]
                return { "Type" : HwType, "Name" : snsr.Hardware.Name, "Sensor" : snsr.Name, "Reading" : u'%s\xb0C' % snsr.Value }


#------------- Obtencion de las temperaturas en forma de diccionario ---------------------------------
    def get_temperatures(self) :

        temperature_list = self.fetch_data(self.init_OHM())

        return temperature_list

class Temperature(Monitor):

    #---------- Temperatura de la CPU --------------------------
    def get_cpu_temperature(self):

        try:
            for item in self.get_temperatures():
                if type(item) == dict:
                    if ('CPU' in item['Type']) and ('CPU Package' in item['Sensor']):
                        return item['Reading'].replace('°C','')
        except:
            return False

    #--------- Temperatura de la GPU --------------------

    def get_gpu_temperature(self):
        try:
            for item in self.get_temperatures():
                if type(item) == dict:
                    if 'Gpu' in item['Type']:
                        return item['Reading'].replace('°C','')
        
        except:
            return False
