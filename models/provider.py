from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    supplier_rank= fields.Integer(string="supplier Rank")
    #Informacion extra
    Codigoproveedor= fields.Char(string="Codigoproveedor")
    Codigocontable= fields.Char(string="Codigocontable")
    Nombrecomercial= fields.Char(string="Nombrecomercial")
    Codigoformapago= fields.Char(string="Codigoformapago")
    ProveedorCEE= fields.Char(string="ProveedorCEE")
    Codigogrupo= fields.Char(string="Codigogrupo")
    Grupocompras= fields.Char(string="Grupocompras")
    Ivafijo= fields.Char(string="Ivafijo")
    Acreedor= fields.Char(string="Acreedor")
    Registrosanitario= fields.Char(string="Registrosanitario")
    Exentoiva= fields.Char(string="Exentoiva")
    
    #Informacion bancaria Extra
    Formadepago= fields.Char(string="Formadepago")
    Direccionbanco= fields.Char(string="Direccionbanco")
    Poblacionbanco= fields.Char(string="Poblacionbanco")
    Provinciabanco= fields.Char(string="Provinciabanco")
    Paisbanco= fields.Char(string="Paisbanco")
    Iban= fields.Char(string="Iban")
    Bic= fields.Char(string="Bic")
    Codigodivisa= fields.Char(string="Codigodivisa")
    
    #Informacion de contacto Extra
    Telefono1= fields.Char(string="Telefono1")
    Fax= fields.Char(string="Fax")
    Personacontacto= fields.Char(string="Personacontacto")
    Aptdocorreos= fields.Char(string="Aptdocorreos")
    Representante1= fields.Char(string="Representante1")
    Representante2= fields.Char(string="Representante2")
    Telefonorep1= fields.Char(string="Telefonorep1")
    Prefijo= fields.Char(string="Prefijo")
    Cpextranjero= fields.Char(string="Cpextranjero")
    # Campo booleano para controlar si la página es visible o no
    show_bank_page = fields.Boolean(name="page_bank_info") 
#Observaciones= fields.Char(string="")
#Preparacion para la base de datos
        #ALTER TABLE res.partner
        #ADD COLUMN Codigoproveedor VARCHAR,
        #ADD COLUMN Codigocontable VARCHAR,
        #ADD COLUMN Telefono1 VARCHAR,
        #ADD COLUMN Fax VARCHAR,
        #ADD COLUMN Personacontacto VARCHAR,
        #ADD COLUMN Formadepago VARCHAR,
        #ADD COLUMN Direccionbanco VARCHAR,
        #ADD COLUMN Poblacionbanco VARCHAR,
        #ADD COLUMN Provinciabanco VARCHAR,
        #ADD COLUMN Paisbanco VARCHAR,
        #ADD COLUMN Nombrecomercial VARCHAR,
        #ADD COLUMN Codigoformapago VARCHAR,
        #ADD COLUMN ProveedorCEE VARCHAR,
        #ADD COLUMN Codigogrupo VARCHAR,
        #ADD COLUMN Grupocompras VARCHAR,
        #ADD COLUMN Aptdocorreos VARCHAR,
        #ADD COLUMN Ivafijo VARCHAR,
        #ADD COLUMN Acreedor VARCHAR,
        #ADD COLUMN Representante1 VARCHAR,
        #ADD COLUMN Representante2 VARCHAR,
        #ADD COLUMN Telefonorep1 VARCHAR,
        #ADD COLUMN Prefijo VARCHAR,
        #ADD COLUMN Cpextranjero VARCHAR,
        #ADD COLUMN Iban VARCHAR,
        #ADD COLUMN Bic VARCHAR,
        #ADD COLUMN Codigodivisa VARCHAR,
        #ADD COLUMN Registrosanitario VARCHAR,
        #ADD COLUMN Exentoiva VARCHAR;