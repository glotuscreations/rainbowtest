# Generated by Django 2.1.1 on 2018-09-28 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_remove_userprofiles_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiles',
            name='preference',
            field=models.CharField(choices=[('gay man looking for another gay man', 'gay man looking for another gay man'), ('bisexual man looking for men and women', 'bisexual man looking for men and women'), ('gay man looking for a lesbian wife', 'gay man looking for a lesbian wife'), ('lesbian woman looking for another lesbian woman', 'lesbian woman looking for another lesbian woman'), ('bisexual woman looking for both men and women', 'bisexual woman looking for both men and women'), ('lesbian woman looking for a gay husband', 'lesbian woman looking for a gay husband'), ('trans/intersex looking for females', 'trans/intersex looking for females'), ('trans/intersex looking for males', 'trans/intersex looking for males'), ('male looking for trans/intersex', 'male looking for trans/intersex'), ('female looking for trans/intersex', 'female looking for trans/intersex'), ('Looking for anyone for friendship', 'Looking for anyone for friendship'), ('Looking to co-parent', 'Looking to co-parent')], max_length=300, null=True, verbose_name='Preference:'),
        ),
    ]