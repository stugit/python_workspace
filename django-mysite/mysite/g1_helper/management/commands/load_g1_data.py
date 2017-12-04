from django.core.management.base import BaseCommand
from g1_helper.models import G1File, G1FileField, G1PostingType, G1FileUploadErrorMessage

import sys


# create a generator to exclude blank lines and lines beginning with a hash
def non_blank_lines(f_in):
    for l in f_in:
        line = l.rstrip()
        if line:
            yield line


# create a generator to exclude comments, lines beginning with a hash
def non_comments(f_in):
    for l in f_in:
        line = l.rstrip()  # remove \n
        if not line.startswith("#"):
            yield line


class Command(BaseCommand):
    args = ""
    help = ""

    def _create_g1_files(self):
        # delete all objects of this type
        G1File.objects.all().delete()

        # Now create them
        f = G1File(filename="TRADE_UPLOAD")
        f.save()
        f = G1File(filename="SETTLEMENT_UPLOAD")
        f.save()
        f = G1File(filename="TRADE_UPLOAD_CONFIRMATION")
        f.save()
        f = G1File(filename="SETTLEMENT_UPLOAD_CONFIRMATION")
        f.save()
        print("G1 files loaded.")


    def _create_g1_file_fields_trade_upload(self):

        # delete all objects of this type
        G1FileField.objects.all().delete()

        filename = G1File.objects.get(filename="TRADE_UPLOAD")
        if not filename:
            print("No such filename! Aborting.")
            sys.exit(1)

        file = "g1_helper/management/data/trade_upload_meta.txt"
        with open(file, 'r', encoding='utf-8-sig') as f_in:
            file_type = ""
            idx = 0
            for x in f_in:
                x = x.rstrip()

                if x.startswith("#"):
                    pass  # skip
                elif x.startswith("TYPE="):
                    tmp_type = x.split('=')
                    file_type = tmp_type[1]
                elif not x:
                    file_type = ""
                    idx = 0

                if x.startswith('|') and file_type:
                    idx = idx + 1
                    fields = x.split('|')
                    o = G1FileField(filename=filename, ftype=file_type, index=idx, desc=fields[1], vdf=fields[2],
                                    struct=fields[3], pos=fields[4], comments=fields[5])
                    o.save()
                    # print("debug: \t" + fields[1])

        f_in.close()
        print("G1 Trade Upload fields loaded.")

        filename = G1File.objects.get(filename="SETTLEMENT_UPLOAD")
        if not filename:
            print("No such filename! Aborting.")
            sys.exit(1)

        file = "g1_helper/management/data/settlement_upload_meta.txt"
        with open(file, 'r', encoding='utf-8-sig') as f_in:
            file_type = ""
            idx = 0
            for x in f_in:
                x = x.rstrip()

                if x.startswith("#"):
                    pass  # skip
                elif x.startswith("TYPE="):
                    tmp_type = x.split('=')
                    file_type = tmp_type[1]
                elif not x:
                    file_type = ""
                    idx = 0

                if x.startswith('|') and file_type:
                    idx = idx + 1
                    fields = x.split('|')
                    o = G1FileField(filename=filename, ftype=file_type, index=idx, desc=fields[1], vdf=fields[2],
                                    struct=fields[3], pos=fields[4], comments=fields[5])
                    o.save()
                    # print("debug: \t" + fields[1])

        f_in.close()
        print("G1 Settlement Upload fields loaded.")

        filename = G1File.objects.get(filename="TRADE_UPLOAD_CONFIRMATION")
        if not filename:
            print("No such filename! Aborting.")
            sys.exit(1)

        file = "g1_helper/management/data/trade_upload_confirmation.txt"
        with open(file, 'r', encoding='utf-8-sig') as f_in:
            file_type = ""
            idx = 0
            for x in f_in:
                x = x.rstrip()

                if x.startswith("#"):
                    pass  # skip
                elif x.startswith("TYPE="):
                    tmp_type = x.split('=')
                    file_type = tmp_type[1]
                elif not x:
                    file_type = ""
                    idx = 0

                if x.startswith('|') and file_type:
                    idx = idx + 1
                    fields = x.split('|')
                    o = G1FileField(filename=filename, ftype=file_type, index=idx, desc=fields[1], vdf="",
                                    struct=fields[2], pos=fields[3], comments=fields[4])
                    o.save()

        f_in.close()
        print("G1 Trade Upload confirmation fields loaded.")

        filename = G1File.objects.get(filename="SETTLEMENT_UPLOAD_CONFIRMATION")
        if not filename:
            print("No such filename! Aborting.")
            sys.exit(1)

        file = "g1_helper/management/data/settlement_upload_confirmation.txt"
        with open(file, 'r', encoding='utf-8-sig') as f_in:
            file_type = ""
            idx = 0
            for x in f_in:
                x = x.rstrip()

                if x.startswith("#"):
                    pass  # skip
                elif x.startswith("TYPE="):
                    tmp_type = x.split('=')
                    file_type = tmp_type[1]
                elif not x:
                    file_type = ""
                    idx = 0

                if x.startswith('|') and file_type:
                    idx = idx + 1
                    fields = x.split('|')
                    o = G1FileField(filename=filename, ftype=file_type, index=idx, desc=fields[1], vdf="",
                                    struct=fields[2], pos=fields[3], comments=fields[4])
                    o.save()

        f_in.close()
        print("G1 Settlement Upload confirmation fields loaded.")


    def _create_g1_posting_types(self):

        # delete all objects of this type
        G1PostingType.objects.all().delete()

        file = "g1_helper/management/data/posting_types.txt"
        with open(file, 'r', encoding='utf-8-sig') as f_in:
            for x in f_in:
                x = x.rstrip()

                if x.startswith("#"):
                    pass  # skip comments
                elif not x:
                    pass  # skip blank lines
                elif x.startswith('|'):
                    fields = x.split('|')
                    o = G1PostingType(posting_type=fields[1], bl=fields[2], description=fields[3])
                    o.save()
        f_in.close()
        print("G1 Posting Types loaded.")

    def _create_g1_file_upload_error_messages(self):
        # delete all objects of this type
        G1FileUploadErrorMessage.objects.all().delete()

        file = "g1_helper/management/data/Trade_Upload_error_messages.txt"

        filename = G1File.objects.get(filename="TRADE_UPLOAD")
        if not filename:
            print("No such filename TRADE_UPLOAD! Aborting.")
            sys.exit(1)

        with open(file, 'r', encoding='utf-8-sig') as f_in:
            for x in f_in:
                x = x.rstrip()

                if x.startswith("#"):
                    pass  # skip comments
                elif not x:
                    pass  # skip blank lines
                elif x.startswith('|'):
                    fields = x.split('|')
                    o = G1FileUploadErrorMessage(filename=filename, code=fields[1], posted=fields[2],
                                                 description=fields[3])
                    o.save()
        f_in.close()
        print("G1 Trade Upload error messages loaded.")

        file = "g1_helper/management/data/Settlement_Upload_error_messages.txt"

        filename = G1File.objects.get(filename="SETTLEMENT_UPLOAD")
        if not filename:
            print("No such filename SETTLEMENT_UPLOAD! Aborting.")
            sys.exit(1)

        with open(file, 'r', encoding='utf-8-sig') as f_in:
            for x in f_in:
                x = x.rstrip()

                if x.startswith("#"):
                    pass  # skip comments
                elif not x:
                    pass  # skip blank lines
                elif x.startswith('|'):
                    fields = x.split('|')
                    o = G1FileUploadErrorMessage(filename=filename, code=fields[1], posted=fields[2],
                                                 description=fields[3])
                    o.save()
        f_in.close()
        print("G1 Settlement Upload error messages loaded.")


    def handle(self, *args, **options):
        self._create_g1_files()
        self._create_g1_file_fields_trade_upload()
        self._create_g1_posting_types()
        self._create_g1_file_upload_error_messages()
