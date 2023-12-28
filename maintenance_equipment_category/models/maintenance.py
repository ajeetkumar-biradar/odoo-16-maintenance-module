from odoo import fields, models, api
import base64
import qrcode
from io import BytesIO


class CustomInherit(models.Model):
    _inherit = 'maintenance.equipment'

    department_id = fields.Many2one('hr.department', string='Department')

    @api.onchange('employee_id')
    def _onchange_employee_id(self):
        if self.employee_id:
            self.department_id = self.employee_id.department_id.id
        else:
            self.department_id = False

    # code of location
    status_location = fields.Selection([
        ('type1', 'Active'),
        ('type2', 'Inactive')
    ], string="Status", required=True)
    postal_code = fields.Char(string="Postal Code")
    city = fields.Char(string="City")
    country = fields.Char(string="Country")
    # end code of location

    # code of NAS
    nas = fields.Selection([
        ('type1', 'NAS storage'),
        ('type2', 'Server1')
    ])
    raid_level = fields.Char(string="RAID Level")
    Size = fields.Char(string="Size")
    # end code of NAS

    # code of lights
    type_lights = fields.Selection([
        ('type1', 'Bulb'),
        ('type2', 'Cfl'),
        ('type3', 'Tube')
    ], string="Type")
    watts = fields.Char(string="Watts")
    # end code of lights

    # code of speakers
    type_speakers = fields.Selection([
        ('type1', 'BIG')
    ], string="Type")
    # end of code speakers

    # code for cctv
    ip_address = fields.Char(string="IP Address")
    # comman code

    # code of PA_sets
    mic = fields.Char(string="Mic")
    # end of code PA_sets

    # code for gadget
    department_gadget = fields.Selection([
        ('type1', 'Accounts'),
        ('type2', 'Agri'),
        ('type3', 'CNC'),
        ('type4', 'core-team'),
        ('type5', 'DAP'),
        ('type6', 'DET-Tech'),
        ('type7', 'DFP'),
        ('type8', 'DIT'),
        ('type9', 'DKF'),
        ('type10', 'DSEP'),
        ('type11', 'DSF'),
        ('type12', 'E&C'),
        ('type13', 'Electrical'),
        ('type14', 'Elevate'),
        ('type15', 'Frontdesk'),
        ('type16', 'HR'),
        ('type17', 'Hostel-warden'),
        ('type18', 'IT'),
        ('type19', 'Leaders'),
        ('type20', 'Operations'),
        ('type21', 'Placements'),
        ('type22', 'Promotion'),
        ('type23', 'S&O'),
        ('type24', 'SIV'),
        ('type25', 'SKC'),
        ('type26', 'Security'),
        ('type27', 'SkillPlus-Hubbli'),
        ('type28', 'Tech'),
        ('type29', 'Telly-Marking'),
        ('type30', 'Yoga'),
    ], string="Department")
    role = fields.Selection([
        ('type1', 'Academic'),
        ('type2', 'Moblization'),
        ('type3', 'Operations'),
        ('type4', 'SIV'),
        ('type5', 'Training'),
    ], string="Role")
    imei = fields.Char(string="IMEI")
    phone_number = fields.Char(string="Phone Number")
    mobile_version = fields.Char(string="Mobile Version")
    brand = fields.Selection([
        ('type1', 'HP'),
        ('type2', 'DELl'),
        ('type3', 'LENOVO')
    ], string="Brand")
    Model = fields.Selection([
        ('type1', 'Optiplex 780'),
        ('type2', 'Optiplex 730'),
        ('type3', 'Optiplex 3040'),
        ('type4', 'Optiplex 5040'),
        ('type5', 'Latitude 7490'),
        ('type6', '840 G3'),
        ('type7', 'Thinkcenter')
    ], string="Model")
    #  end of code gadget

    # code for move to date
    move_to_production = fields.Date(string="Move To Producation Date ")
    move_two_stock = fields.Date(string="Move2Stock")
    #  end of code for move to date

    invoice_no = fields.Char(string="Invoice No")

    type_screen = fields.Selection([
        ('type1', 'Screen')
    ], string="Type")

    # status = fields.Selection([
    #     ('type1', 'Repair'),
    #     ('type2', 'Damage')
    # ], string="Status")
    # brand=fields.Char(string="Brand")
    # comman code end here

    os_family = fields.Selection([
        ('type1', 'windows'),
        ('type2', 'mac'),
        ('type3', 'linux'),
        ('type4', 'Windows-Profational'),
        ('type5', 'Windows-Home')
    ], string="Os family")
    os_version = fields.Selection([
        ('type1', 'windows 1'),
        ('type2', 'mac 1'),
        ('type3', 'Windows7'),
        ('type4', 'Windows10'),
        ('type5', 'Windows11')
    ], string="Os version")
    cpu = fields.Char(string="CPU")
    ram = fields.Char(string="RAM")
    Invoice_no = fields.Integer(string="Invoice No")
    Asset_no = fields.Char(string="Serial Number", required=True)

    Department = fields.Selection([
        ('type1', 'DF'),
        ('type2', 'DF rttc')
    ], string="Department")
    hdd = fields.Char(string="HDD")
    # equipment_category = fields.Selection([
    #     ('type1', 'Desktop'),
    #     ('type3', 'Fans'),
    #     ('type4', 'Monitors'),
    #     ('type5', 'CPU'),
    #     ('type6', 'Fire extinguisher'),
    #     ('type7', 'Chairs'),
    #     ('type8', 'PC Software'),
    #     ('type9', 'Screen'),
    #     ('type11', 'Laptop'),
    #     ('type12', 'Printer'),
    #     ('type13', 'Tablet'),
    #     ('type14', 'PA_sets'),
    #     ('type15', 'CCTV'),
    #     ('type16', 'SAN switch'),
    #     ('type17', 'AC'),
    #     ('type18', 'Mike'),
    #     ('type19', 'PDU'),
    #     ('type20', 'HDD'),
    #     ('type21', 'Router'),
    #     ('type22', 'projector'),
    #     ('type23', 'Scanner'),
    #     ('type24', 'switches'),
    #     ('type25', 'Location'),
    #     ('type26', 'Network Device'),
    #     ('type27', 'Speaker'),
    #     ('type28', 'Walky_Talky'),
    #     ('type29', 'Access_points'),
    #     ('type30', 'Lights'),
    #     ('type31', 'Podium'),
    #     ('type32', 'Cupboard'),
    #     ('type33', 'Stell_Watertank'),
    #     ('type34', 'Rack'),
    #     ('type35', 'Cot'),
    #     ('type36', 'Board'),
    #     ('type37', 'Peripheral'),
    #     ('type38', 'Mobile Phone'),
    #     ('type39', 'Storage System'),
    #     ('type40', 'Amplifier'),
    #     ('type41', 'Telivision'),
    #     ('type42', 'Biometric'),
    #     ('type43', 'Receiver'),
    #     ('type44', 'NAS File System'),
    #     ('type45', 'NAS'),
    #     ('type46', 'Storage System'),
    #     ('type47', 'Hotspot')
    # ], string="Equipment_category")
    # equipment_category=fields.Many2one('maintenance.equipment.category',string="Equipment Category")
    type_fans = fields.Selection([
        ('type1', 'HP'),
        ('type2', 'DELL')
    ], string="Type")
    document_ids = fields.Many2many('ir.attachment', string='Documents')

    count = fields.Integer(string="Number of request", compute="_compute_maintenance_count")

    organization = fields.Selection([
        ('type1', 'Deshpande Startups'),
        ('type2', 'Deshpande Foundation'),
        ('type3', 'Deshpande Skilling')
    ], string="Organization", required=True)

    Business_criticity = fields.Selection([
        ('type1', 'high'),
        ('type2', 'medium'),
        ('type3', 'low')
    ], string="Business Criticity", required=True)
    type = fields.Selection([
        ('type1', '10KG'),
        ('type2', '2KG'),
        ('type3', '4.5KG'),
        ('type4', '5KG')
    ], string="Type")
    type_chairs = fields.Selection([
        ('type1', 'Benches'),
        ('type2', 'Black'),
        ('type3', 'Blue'),
        ('type4', 'Brown')
    ], string="Type")
    type_fans = fields.Selection([
        ('type1', 'Table'),
        ('type2', 'ceiling'),
        ('type3', 'standfans'),
        ('type4', 'walifan')
    ], string="Type")
    rack = fields.Selection([
        ('type1', 'media power extension '),
        ('type2', 'power extension'),
        ('type3', 'switch'),
        ('type4', 'switch board')
    ], string="Rack")

    # name = fields.Char(string='Name', required=True)
    barcode = fields.Binary(string='Barcode', compute='_compute_barcode')

    @api.depends('asset_number')
    def _compute_barcode(self):
        for record in self:
            # data1=record.name_seq
            # data2=record.Asset_number
            delimiter = '|'
            combined_data = delimiter.join(
                ['Asset Number ' + str(record.asset_number) + '  ||  ', 'Serial Number ' + str(record.Asset_no)])
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(combined_data)
            qr.make(fit=True)
            img = qr.make_image(fill_color='black', back_color='white')
            img_buffer = BytesIO()
            img.save(img_buffer, format='PNG')
            record.barcode = base64.b64encode(img_buffer.getvalue())

    def _compute_maintenance_count(self):
        for equipment in self:
            equipment.count = self.env['maintenance.request'].search_count([('equipment_id', '=', equipment.id)])

    charger_serial_no = fields.Char(string="Charger Serial No")
    asset_number = fields.Char(string='Asset Number', readonly=True, copy=False)

    def _compute_asset_number(self):
        for record in self:
            sequence = self.env['ir.sequence'].next_by_code('maintenance.equipment.asset_number') or '/'
            record.asset_number = sequence

    def _create_asset_number(self):
        for record in self:
            if not record.asset_number:
                record._compute_asset_number()

    @api.model
    def create(self, vals):
        record = super(CustomInherit, self).create(vals)
        record._create_asset_number()
        return record
