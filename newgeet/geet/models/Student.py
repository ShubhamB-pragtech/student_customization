from odoo import models, fields,api
class Student(models.Model):
    _name = 'geet.student'
    _description = 'Student'
    name = fields.Char(string="Name")
    classes = fields.Char(string="class")
    age = fields.Integer(string="age")
    status = fields.Selection([('public', 'Public',), ('private', 'Private')], string="status", readonly=True,
                              default="private")

    def orm_method(self):
        search_var = self.env['geet.student'].browse([4])
        for rec in search_var:
            print("name is:",rec.name,"age is:",rec.age)
        print("orm", search_var)
        # search([('name', '=', 'shubham')]) this line print only who name is shubham(hear use domain)

    def orm_create_method(self):
        create_var = self.env['geet.student'].create({
            "name":'ganesh',
            "classes" :'pragmatic',
            "age" :'20'
        })
        print(create_var)

    def orm_write_method(self):
        write_id=self.env['geet.student'].browse(10)
        write_id.write({
            "name":'ganesh bhahu',
            "classes":'ty',
            "age":'22'
        })
    def orm_unlink_method(self):
        unlink_var = self.env['geet.student'].browse(10)
        unlink_var.unlink()
