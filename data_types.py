import datetime

class MasterRecord:
    def __init__(self) -> None:
        self.docNum = ''
        self.warehouse = ''
        self.terminal = ''
        self.vesselName = ''
        self.deliveryDate = datetime.datetime(1944, 9, 9)
        self.itemCode = ''
        self.avizNo = 0
        self.fertilizer = ''
        self.truckGross = 0.0
        self.truckTara = 0.0
        self.truckNeto = 0.0
        self.nrOfBB = 0.0
        self.cargoNetMts = 0.0
        self.loadPortName = ''
        self.dischargingPlace = ''
        self.transportNo = ''
        self.releaseDate = datetime.datetime(1944, 9, 9)
        self.releaseNo = ''
        self.cardName = ''
        self.contractNo = ''

        #
        masterSheetName = ''

masterRecordColumns = [
    ['docNum',              ('A', 'Doc Num')],
    ['warehouse',           ('B', 'Warehouse')],
    ['terminal',            ('C', 'Terminal')],
    ['vesselName',          ('D', 'Vessel Name')],
    ['deliveryDate',        ('E', 'Delivery date')],
    ['itemCode',            ('F', 'Item Code')],
    ['avizNo',              ('G', 'Aviz No.')],
    ['fertilizer',          ('H', 'Fertilizer')],
    ['truckGross',          ('I', 'Truck gross (mt)')],
    ['truckTara',           ('J', 'Truck tara (mt)')],
    ['truckNeto',           ('K', 'Truck net (mt)')],
    ['nrOfBB',              ('L', 'Nr. of BB')],
    ['cargoNetMts',         ('M', 'Cargo net (mts)')],
    ['loadPortName',        ('N', 'Load Port Name')],
    ['dischargingPlace',    ('O', 'Discharging place')],
    ['transportNo',         ('P', 'Transport No.')],
    ['releaseDate',         ('Q', 'Release date')],
    ['releaseNo',           ('R', 'Released No.')],
    ['cardName',            ('S', 'CardName')],
    ['contractNo',          ('T', 'Contract No')]
]






