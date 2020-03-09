class EmailValidator:
    def __init__(self, min_length: int, mails: [], domains: []):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name):
        """
        returns whether the name is greater than or equal to
        the min_length
        """
        return self.min_length <= len(name)

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains

    def __get_email_parts(self, email):
        valid_domains = ['.co.uk']
        at_index = email.index("@")
        dot_index = email.rindex(".")

        name = email[:at_index]
        mail = email[at_index + 1:dot_index]
        domain = email[dot_index + 1:]

        result = list(filter(lambda valid_domain: email.endswith(valid_domain), valid_domains))
        if result:
            domain = result[0]
            mail = email[at_index + 1:-len(domain)]

        return (name, mail, domain)

    def validate(self, email):
        (name, mail, domain) = self.__get_email_parts(email)

        return self.__validate_name(name) and \
               self.__validate_mail(mail) and \
               self.__validate_domain(domain)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.com"))
print(email_validator.validate("abv@softuni.bg"))
