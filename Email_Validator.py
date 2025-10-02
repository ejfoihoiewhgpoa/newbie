class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains
    
    def validate_name(self, name):
        return len(name) >= self.min_length
    def validate_mail(self, mails):
        return mails in self.mails
    def validate_domain(self, domains):
        return domains in self.domains
    def validate(self, email):
        name, rest = email.split("@")
        mail, domain = rest.split(".")
        return (self.validate_name(name) and self.validate_mail(mail) and self.validate_domain(domain))
mails  = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
