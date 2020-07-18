import math
import argparse
import sys


# def check_positive(value):
#     checking_value = value
#     if type(value) is int:
#         if value <= 0:
#             raise argparse.ArgumentTypeError("Incorrect parameters")
#         else:
#             checking_value = value
#     if type(value) is float:
#         if value <= 0.00:
#             raise argparse.ArgumentTypeError("Incorrect parameters")
#         else:
#             checking_value = value
#     return checking_value


def calculate_differentiated_payments(prncpl, prds, intrst):
    current_period = 1
    credit_interest = intrst / 100 / 12
    overpayment = 0
    sum_of_diffpayment = 0
    for i in range(0, prds):
        diffpayment = prncpl / prds + credit_interest * (prncpl - (prncpl * (current_period - 1) / prds))
        print("Month ", current_period, " : paid out ", math.ceil(diffpayment))
        sum_of_diffpayment += math.ceil(diffpayment)
        current_period += 1
    overpayment += prds * sum_of_diffpayment / prds - prncpl
    print("Overpayment = ", round(overpayment))


def calculate_annuity_payments(prncpl, prds, intrst):
    credit_interest = intrst / 100 / 12
    growth_count = (credit_interest * math.pow(1 + credit_interest, prds)) / (math.pow(1 + credit_interest, prds) - 1)
    monthly_payment = prncpl * growth_count
    print('Your annuity payment = ', math.ceil(monthly_payment), '!')
    overpayment = abs(prds * math.ceil(monthly_payment) - prncpl)
    print("Overpayment = ", round(overpayment))


def calculate_principal(intrst, prds, pmnt):
    credit_interest = intrst / 100 / 12
    growth_count = (credit_interest * math.pow(1 + credit_interest, prds)) / (math.pow(1 + credit_interest, prds) - 1)
    credit_principal = pmnt / growth_count
    print('Your credit principal = ', math.floor(credit_principal), '!')
    overpayment = abs(prds * math.floor(pmnt) - credit_principal)
    print("Overpayment = ", math.ceil(overpayment))


def calculate_periods(intrst, prncpl, pmnt):
    credit_interest = intrst / 100 / 12
    base = 1 + credit_interest
    x = pmnt / (pmnt - credit_interest * prncpl)
    count_of_months = math.log(x, base)
    if count_of_months > 12 and count_of_months % 12 != 0:
        years = count_of_months // 12
        months = count_of_months % 12
        if math.ceil(months) == 12:
            print('You need ', math.floor(years) + 1, 'years to repay this credit!')
        else:
            print('You need ', math.floor(years), ' years and ', math.ceil(months), ' months to repay this credit!')
    elif count_of_months > 12 and count_of_months % 12 == 0:
        years = count_of_months // 12
        print('You need ', round(years), 'years to repay this credit!')
    elif count_of_months < 12:
        print('You need ', count_of_months, ' months to repay this credit!')
    overpayment = math.ceil(count_of_months) * math.floor(pmnt) - prncpl
    print("Overpayment = ", math.ceil(overpayment))


parser = argparse.ArgumentParser(description="Credit Calculator")
parser.add_argument("--type", type=str, help="type of credit")
parser.add_argument("--principal", type=float, help="credit principal")
parser.add_argument("--periods", type=int, help="count of periods")
parser.add_argument("--interest", type=float, help="credit interest")
parser.add_argument("--payment", type=float, help="monthly payment")
args = parser.parse_args()

typeCheck = ["diff", "annuity"]
annualPaymentCheck = ["principal", "periods", "interest"]

if args.type is None:
    print("Incorrect parameters")
elif args.type not in typeCheck:
    print("Incorrect parameters")
elif args.type == "diff":
    if args.payment is not None:
        print("Incorrect parameters")
    elif len(sys.argv) < 5:
        print("Incorrect parameters")
    else:
        if args.principal <= 0 or args.periods <= 0 or args.interest <= 0:
            print("Incorrect parameters")
        else:
            calculate_differentiated_payments(args.principal, args.periods, args.interest)
elif args.type == "annuity":
    if args.interest is None:
        print("Incorrect parameters")
    elif len(sys.argv) < 5:
        print("Incorrect parameters")
    else:
        if args.payment is None and args.principal > 0 and args.periods > 0 and args.interest > 0:
            calculate_annuity_payments(args.principal, args.periods, args.interest)
        elif args.principal is None and args.interest > 0 and args.periods > 0 and args.payment > 0:
            calculate_principal(args.interest, args.periods, args.payment)
        elif args.periods is None and args.interest > 0 and args.principal > 0 and args.payment > 0:
            calculate_periods(args.interest, args.principal, args.payment)
        else:
            print("Incorrect parameters")
