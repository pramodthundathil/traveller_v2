
from importlib.resources import Package
from django.contrib import messages
from django.shortcuts import redirect, render
from packages.models import Packages
from .models import BookingPackage

from django.contrib.auth.decorators import login_required

import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

from django.conf import settings
from django.core.mail import send_mail,EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string



# Create your views here.
@login_required(login_url='signup')
def booking_form(request):
    
    package_id = request.POST["submit"]
    packages = Packages.objects.filter(Package_id = package_id) 
    cont = {'AF': 'Afghanistan', 'AX': 'Åland Islands', 'AL': 'Albania', 'DZ': 'Algeria', 'AS': 'American Samoa', 'AD': 'Andorra', 'AO': 'Angola', 'AI': 'Anguilla', 'AQ': 'Antarctica', 'AG': 'Antigua and Barbuda', 'AR': 'Argentina', 'AM': 'Armenia', 'AW': 'Aruba', 'AU': 'Australia', 'AT': 'Austria', 'AZ': 'Azerbaijan', 'BS': 'Bahamas', 'BH': 'Bahrain', 'BD': 'Bangladesh', 'BB': 'Barbados', 'BY': 'Belarus', 'BE': 'Belgium', 'BZ': 'Belize', 'BJ': 'Benin', 'BM': 'Bermuda', 'BT': 'Bhutan', 'BO': 'Bolivia (Plurinational State of)', 'BQ': 'Bonaire, Sint Eustatius and Saba', 'BA': 'Bosnia and Herzegovina', 'BW': 'Botswana', 'BV': 'Bouvet Island', 'BR': 'Brazil', 'IO': 'British Indian Ocean Territory', 'BN': 'Brunei Darussalam', 'BG': 'Bulgaria', 'BF': 'Burkina Faso', 'BI': 'Burundi', 'CV': 'Cabo Verde', 'KH': 'Cambodia', 'CM': 'Cameroon', 'CA': 'Canada', 'KY': 'Cayman Islands', 'CF': 'Central African Republic', 'TD': 'Chad', 'CL': 'Chile', 'CN': 'China', 'CX': 'Christmas Island', 'CC': 'Cocos (Keeling) Islands', 'CO': 'Colombia', 'KM': 'Comoros', 'CD': 'Congo (the Democratic Republic of the)', 'CG': 'Congo', 'CK': 'Cook Islands', 'CR': 'Costa Rica', 'CI': "Côte d'Ivoire", 'HR': 'Croatia', 'CU': 'Cuba', 'CW': 'Curaçao', 'CY': 'Cyprus', 'CZ': 'Czechia', 'DK': 'Denmark', 'DJ': 'Djibouti', 'DM': 'Dominica', 'DO': 'Dominican Republic', 'EC': 'Ecuador', 'EG': 'Egypt', 'SV': 'El Salvador', 'GQ': 'Equatorial Guinea', 'ER': 'Eritrea', 'EE': 'Estonia', 'SZ': 'Eswatini', 'ET': 'Ethiopia', 'FK': 'Falkland Islands  [Malvinas]', 'FO': 'Faroe Islands', 'FJ': 'Fiji', 'FI': 'Finland', 'FR': 'France', 'GF': 'French Guiana', 'PF': 'French Polynesia', 'TF': 'French Southern Territories', 'GA': 'Gabon', 'GM': 'Gambia', 'GE': 'Georgia', 'DE': 'Germany', 'GH': 'Ghana', 'GI': 'Gibraltar', 'GR': 'Greece', 'GL': 'Greenland', 'GD': 'Grenada', 'GP': 'Guadeloupe', 'GU': 'Guam', 'GT': 'Guatemala', 'GG': 'Guernsey', 'GN': 'Guinea', 'GW': 'Guinea-Bissau', 'GY': 'Guyana', 'HT': 'Haiti', 'HM': 'Heard Island and McDonald Islands', 'VA': 'Holy See', 'HN': 'Honduras', 'HK': 'Hong Kong', 'HU': 'Hungary', 'IS': 'Iceland', 'IN': 'India', 'ID': 'Indonesia', 'IR': 'Iran (Islamic Republic of)', 'IQ': 'Iraq', 'IE': 'Ireland', 'IM': 'Isle of Man', 'IL': 'Israel', 'IT': 'Italy', 'JM': 'Jamaica', 'JP': 'Japan', 'JE': 'Jersey', 'JO': 'Jordan', 'KZ': 'Kazakhstan', 'KE': 'Kenya', 'KI': 'Kiribati', 'KP': "Korea (the Democratic People's Republic of)", 'KR': 'Korea (the Republic of)', 'KW': 'Kuwait', 'KG': 'Kyrgyzstan', 'LA': "Lao People's Democratic Republic", 'LV': 'Latvia', 'LB': 'Lebanon', 'LS': 'Lesotho', 'LR': 'Liberia', 'LY': 'Libya', 'LI': 'Liechtenstein', 'LT': 'Lithuania', 'LU': 'Luxembourg', 'MO': 'Macao', 'MK': 'Macedonia (the former Yugoslav Republic of)', 'MG': 'Madagascar', 'MW': 'Malawi', 'MY': 'Malaysia', 'MV': 'Maldives', 'ML': 'Mali', 'MT': 'Malta', 'MH': 'Marshall Islands', 'MQ': 'Martinique', 'MR': 'Mauritania', 'MU': 'Mauritius', 'YT': 'Mayotte', 'MX': 'Mexico', 'FM': 'Micronesia (Federated States of)', 'MD': 'Moldova (the Republic of)', 'MC': 'Monaco', 'MN': 'Mongolia', 'ME': 'Montenegro', 'MS': 'Montserrat', 'MA': 'Morocco', 'MZ': 'Mozambique', 'MM': 'Myanmar', 'NA': 'Namibia', 'NR': 'Nauru', 'NP': 'Nepal', 'NL': 'Netherlands', 'NC': 'New Caledonia', 'NZ': 'New Zealand', 'NI': 'Nicaragua', 'NE': 'Niger', 'NG': 'Nigeria', 'NU': 'Niue', 'NF': 'Norfolk Island', 'MP': 'Northern Mariana Islands', 'NO': 'Norway', 'OM': 'Oman', 'PK': 'Pakistan', 'PW': 'Palau', 'PS': 'Palestine, State of', 'PA': 'Panama', 'PG': 'Papua New Guinea', 'PY': 'Paraguay', 'PE': 'Peru', 'PH': 'Philippines', 'PN': 'Pitcairn', 'PL': 'Poland', 'PT': 'Portugal', 'PR': 'Puerto Rico', 'QA': 'Qatar', 'RE': 'Réunion', 'RO': 'Romania', 'RU': 'Russian Federation', 'RW': 'Rwanda', 'BL': 'Saint Barthélemy', 'SH': 'Saint Helena, Ascension and Tristan da Cunha', 'KN': 'Saint Kitts and Nevis', 'LC': 'Saint Lucia', 'MF': 'Saint Martin (French part)', 'PM': 'Saint Pierre and Miquelon', 'VC': 'Saint Vincent and the Grenadines', 'WS': 'Samoa', 'SM': 'San Marino', 'ST': 'Sao Tome and Principe', 'SA': 'Saudi Arabia', 'SN': 'Senegal', 'RS': 'Serbia', 'SC': 'Seychelles', 'SL': 'Sierra Leone', 'SG': 'Singapore', 'SX': 'Sint Maarten (Dutch part)', 'SK': 'Slovakia', 'SI': 'Slovenia', 'SB': 'Solomon Islands', 'SO': 'Somalia', 'ZA': 'South Africa', 'GS': 'South Georgia and the South Sandwich Islands', 'SS': 'South Sudan', 'ES': 'Spain', 'LK': 'Sri Lanka', 'SD': 'Sudan', 'SR': 'Suriname', 'SJ': 'Svalbard and Jan Mayen', 'SE': 'Sweden', 'CH': 'Switzerland', 'SY': 'Syrian Arab Republic', 'TW': 'Taiwan (Province of China)', 'TJ': 'Tajikistan', 'TZ': 'Tanzania, United Republic of', 'TH': 'Thailand', 'TL': 'Timor-Leste', 'TG': 'Togo', 'TK': 'Tokelau', 'TO': 'Tonga', 'TT': 'Trinidad and Tobago', 'TN': 'Tunisia', 'TR': 'Turkey', 'TM': 'Turkmenistan', 'TC': 'Turks and Caicos Islands', 'TV': 'Tuvalu', 'UG': 'Uganda', 'UA': 'Ukraine', 'AE': 'United Arab Emirates', 'GB': 'United Kingdom of Great Britain and Northern Ireland', 'UM': 'United States Minor Outlying Islands', 'US': 'United States of America', 'UY': 'Uruguay', 'UZ': 'Uzbekistan', 'VU': 'Vanuatu', 'VE': 'Venezuela (Bolivarian Republic of)', 'VN': 'Viet Nam', 'VG': 'Virgin Islands (British)', 'VI': 'Virgin Islands (U.S.)', 'WF': 'Wallis and Futuna', 'EH': 'Western Sahara', 'YE': 'Yemen', 'ZM': 'Zambia', 'ZW': 'Zimbabwe'}   
    print(cont.values())
    contries = cont.values()
    return render(request,"booking/booking_form.html",{'packages': packages,"contries":contries})

razorpay_client = razorpay.Client(
  auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

#Booking confirmation...............

@login_required(login_url='signup')
def booking_create(request):
    
    package_id = request.POST["submit"]
    customer_fullname = request.POST["fname"]
    guest_count = request.POST["gcount"]
    infent_number = request.POST["ccount"]
    start_date = request.POST["sdate"]
    end_date = request.POST["Edate"]
    phone_number = request.POST['pnumber']
    email = request.POST['email']
    address = request.POST['Address']
    locality = request.POST['locality']
    state = request.POST['state']
    contry = request.POST['contry']
    
    booking = BookingPackage.objects.create(Package_id = package_id,customer_id = request.user,Name = customer_fullname,Number_of_Gusts = guest_count,Number_of_Gusts_below5 = infent_number,Address_House = address ,Locality = locality ,state = state,Country = contry,phone = phone_number,email = email ,trip_start_date = start_date ,Payment_amount =False,approval_status = False)
    booking.save()
    
    
    packages = Packages.objects.filter(Package_id = package_id)
    package = Packages.objects.get(Package_id = package_id) 
    price = package.Package_price
    
    total_amount = float(price) * int(guest_count) + float(price)/2 * int(infent_number)
    
    booking_id = booking.Bookingid
    
    # Email Confirmation....................
    
    current_site = get_current_site(request)
    mail_subject = 'Booking Confirmation From Traveller'
    message = render_to_string('emailbody.html', {'user': customer_fullname,
                                                  'domain': current_site.domain,
                                                  'booking_id':booking_id,
                                                  'packages':packages,
                                                  'total_amount':total_amount
                                                  })

    email = EmailMessage(mail_subject, message, to=[email])
    email.send(fail_silently=True)
    
    currency = 'INR'
    amount = total_amount * 100 # Rs. 200

  # Create a Razorpay Order Pyament Integration.....
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                          currency=currency,
                          payment_capture='0'))

  # order id of newly created order.
    razorpay_order_id = razorpay_order["id"]
    callback_url = 'paymenthandler/'

  # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
    context['Packages'] = packages
    context['booking'] = booking
    context['total_amount'] = total_amount
    
    
    return render(request,"booking/payment.html",context)

@login_required(login_url='signup')
def update_booking(request):
    bookings = BookingPackage.objects.all()
    
    if request.method == "POST":
        booking_id = request.POST['submit']
        booking = BookingPackage.objects.filter(Bookingid=booking_id)
        bookings = BookingPackage.objects.get(Bookingid=booking_id)
        package_id = bookings.Package_id
        package = Packages.objects.filter(Package_id = package_id )
        return render(request,"booking/edit_booking.html",{"booking":booking,"package":package})
    
    return render(request,'booking/update_booking.html',{"bookings":bookings})

@login_required(login_url='signup')
def approve_booking(request):
    
    booking_id = request.POST['submit']
    booking = BookingPackage.objects.get(Bookingid=booking_id)
    booking.Payment_status = True
    booking.save()
    return redirect ('update_booking')

@login_required(login_url='signup')
def reject_booking(request):
    
    booking_id = request.POST['submit']
    booking = BookingPackage.objects.get(Bookingid=booking_id)
    booking.Payment_status = False
    booking.save()
    return redirect ('update_booking')
@login_required(login_url='signup')
def pending_booking(request):
    
    booking_id = request.POST['submit']
    booking = BookingPackage.objects.get(Bookingid=booking_id)
    booking.Payment_status = None
    booking.save()
    return redirect ('update_booking')

@login_required(login_url='signup')
def customer_booking(request):
    
    user = request.user
    bookings = BookingPackage.objects.filter(customer_id = user)
    
    if request.method == 'POST':
        
        booking_id = request.POST['submit']
        booking = BookingPackage.objects.get(Bookingid=booking_id)
        booking.Payment_status = None
        booking.save()
        return redirect ('customer_booking')
    
    return render(request,'booking/customer_booking.html',{"bookings":bookings})

@login_required(login_url="signup")
def delete_booking(request):
    
    booking_id = request.POST['submit']
    booking = BookingPackage.objects.get(Bookingid=booking_id)
    booking.delete()
    messages.info(request,"Booking Deleted successfuly")
    return redirect ('update_booking')

@csrf_exempt
def paymenthandler(request):

  # only accept POST request.
  if request.method == "POST":
    try:
    
      # get the required parameters from post request.
      payment_id = request.POST.get('razorpay_payment_id', '')
      razorpay_order_id = request.POST.get('razorpay_order_id', '')
      signature = request.POST.get('razorpay_signature', '')
      params_dict = {
        'razorpay_order_id': razorpay_order_id,
        'razorpay_payment_id': payment_id,
        'razorpay_signature': signature
      }

      # verify the payment signature.
      result = razorpay_client.utility.verify_payment_signature(
        params_dict)
      if result is None:
        amount = 2000 # Rs. 200
        try:

          # capture the payemt
          razorpay_client.payment.capture(payment_id, amount)

          # render success page on successful caputre of payment
          return render(request, 'paymentsuccess.html')
        except:

          # if there is an error while capturing payment.
          return render(request, 'paymentfail.html')
      else:

        # if signature verification fails.
        return render(request, 'paymentfail1.html')
    except:

      # if we don't find the required parameters in POST data
      return HttpResponseBadRequest()
  else:
  # if other than POST request is made.
    return HttpResponseBadRequest()
def BookingCancelbyCustomer(request,pk):
      BookingPackage.objects.get(Bookingid = pk).delete()
      messages.info(request,"Booking Cancelled")
      
      return redirect("customer_booking")    
    
        
