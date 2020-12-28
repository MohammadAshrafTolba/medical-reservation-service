from AppSrc.models import specializations


class SpecializationHandler:

    def get_specializations(self):
        return specializations

    def add_specialization(self, specialization):
        if specialization in specializations:
            return False
        
        specializations.append(specialization)
        return True