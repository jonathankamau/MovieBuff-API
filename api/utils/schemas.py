from marshmallow import Schema, fields, validate


class RegisterUserSchema(Schema):
    """ schema for register user resource"""
    first_name = fields.String(required=True, load_only=True,
                               validate=[validate.Length(min=1, max=64),
                                         validate.Regexp(r"[a-zA-Z]*$",
                                                        error=("Firstname must be "
                                                               "made up of letters!"))],
                              error_messages={'required': 'firstname cannot be blank'})
    last_name = fields.String(required=True,
                             load_only=True,
                             validate=[validate.Length(min=1, max=64)],
                             error_messages={'required': 'lastname cannot be blank'})
    username = fields.String(required=True,
                             load_only=True,
                             validate=[validate.Length(min=1, max=64)],
                             error_messages={'required': 'username cannot be blank'})
    password = fields.String(required=True,
                             load_only=True,
                             validate=[validate.Length(min=8)],
                             error_messages={'required': 'password cannot be blank'})


class UserLoginSchema(Schema):
    """ schema for user login resource"""
    username = fields.String(required=True,
                             load_only=True,
                             validate=[validate.Length(min=1, max=64),
                                       validate.Regexp(r"[a-zA-Z]*$",
                                                       error=("Username must be "
                                                              "made up of letters!"))])
    password = fields.String(required=True,
                             load_only=True,
                             validate=[validate.Length(min=8)],
                             error_messages={'required': 'password cannot be blank'})


reg_schema = RegisterUserSchema()
login_schema = UserLoginSchema()
