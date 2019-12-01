from django.db import models


class CustomerRelationsCode(models.Model):
    cr_code_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cr_code_name


class CustomerRelationsJobStatus(models.Model):
    customer_relations_job_status_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_relations_job_status_name


class CustomerRelationsDate(models.Model):
    customer_relations_date_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_relations_date_name


class CustomerRelationsPhoneNumber(models.Model):
    customer_relations_phone_number_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_relations_phone_number_name


class CustomerRelationsExtraRegistrationNumber(models.Model):
    customer_relations_extra_registration_number_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_relations_extra_registration_number_name


class CustomerRelationsVehicleRegistrationNumber(models.Model):
    customer_relations_vehicle_registration_number_name = models.CharField(
        max_length=250
    )
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_relations_vehicle_registration_number_name


class CustomerRelationsJobAuthorizationNumber(models.Model):
    customer_relations_job_authorization_number_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_relations_job_authorization_number_name


class CustomerRelationsWorkshop(models.Model):
    customer_relations_workshop_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_relations_workshop_name


class CustomerRelationsJobApprovedDate(models.Model):
    customer_relations_job_approved_date_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_relations_job_approved_date_name


class CustomerRelationsReason(models.Model):
    customer_relations_reason_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_relations_reason_name


class CustomerRelationsComments(models.Model):
    customer_relations_comments_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_relations_comments_name


class CustomerRelationsDescription(models.Model):
    customer_relations_description_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_relations_description_name


class CustomerRelations(models.Model):
    customer_relations_cr_code = models.CharField(max_length=60)
    customer_relations_job_status = models.CharField(max_length=60)
    customer_relations_date = models.CharField(max_length=60)
    customer_relations_phone_number = models.CharField(max_length=60)
    customer_relations_extra_registration_number = models.CharField(max_length=60)
    customer_relations_vehicle_registration_number = models.CharField(max_length=60)
    customer_relations_job_authorization_number = models.CharField(max_length=60)
    customer_relations_workshop = models.CharField(max_length=60)
    customer_relations_job_approved_date = models.CharField(max_length=60)
    customer_relations_reason = models.CharField(max_length=60)
    customer_relations_comments = models.CharField(max_length=60)
    customer_relations_description = models.CharField(max_length=60)

