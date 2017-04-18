
STATUS_TYPE_ACTIVE = 'A'
STATUS_TYPE_INACTIVE = 'I'

STATUS_CHOICES = (
    (STATUS_TYPE_ACTIVE, 'Active'),
    (STATUS_TYPE_ACTIVE, 'Inactive'),
)

INSTITUTE_TYPE_SYSTEM = 'S'
INSTITUTE_TYPE_APPLICATION = 'A'

INSTITUTE_TYPE_CHOICES = (
		(INSTITUTE_TYPE_SYSTEM, 'System'),
		(INSTITUTE_TYPE_APPLICATION, 'Application'),
	)

GENDER_TYPE_FEMALE = 'F'
GENDER_TYPE_MALE = 'M'

GENDER_CHOICES = (
    (GENDER_TYPE_FEMALE, 'Female'),
    (GENDER_TYPE_MALE, 'Male'),
)

CONTACT_TYPE_PERSONAL = 'P'
CONTACT_TYPE_OFFICE = 'O'
CONTACT_TYPE_LANDLINE = 'L'


CONTACT_CHOICES = (
    (CONTACT_TYPE_PERSONAL, 'Personal'),
    (CONTACT_TYPE_OFFICE, 'Office'),
    (CONTACT_TYPE_LANDLINE,'Landline'),
)