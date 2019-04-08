#import csv
#import os
import math

DECIMAL_MARGIN_GROWTH = 0.000000005
DECIMAL_REV_GROWTH    = 0.02
BOND_DURATION = 5

years_list             = [3      , 5      , 7      , 10 ]
init_margins_list      = [0.16   , 0.18   , 0.2    , 0.22]
sale_EBITDA_list       = [5      , 6      , 7      , 10 ]
init_EBITDA_list            = [4      , 5      , 6      ]
commission_rate_list        = [0.1    , 0.12   , 0.15   ]
interest_rate_list          = [0.07   , 0.08   , 0.09   ]
init_revenue_list           = [1000000, 1500000, 2000000]




def format_header():
	print("---------------------------------------------------------------------------------------------------------")
	print("YR  REVENUE    MARGINS  xBUY   BUY PRICE    YR.EBITDA  TOT.EB.   TOT.REV.    INTEREST/FEES  xSALE  PROFIT")

def grow_margins(decimal_margins,DECIMAL_MARGIN_GROWTH):
	#margins will not grow beyond 0.25
	max_margins = 0.225
	margins = decimal_margins
	margin_growth = DECIMAL_MARGIN_GROWTH 
	new_margins = ( margins + (margins * DECIMAL_MARGIN_GROWTH))

	if new_margins < max_margins:
		return new_margins #returns 0.xx
	else:
		return max_margins #returns 0.25
			
def year_one_simulation(init_revenue,init_margins,init_EBITDA):	
	revenue = init_revenue
	margins = init_margins #0.xx
	buy_price = init_revenue * init_margins * init_EBITDA

	EBITDA = revenue * init_margins
 
	tot_EBITDA = EBITDA	
	tot_revenue = revenue

	print(f"1  {revenue:,.0f}    {margins*100:.3f}           {buy_price:,.0f}     {EBITDA:,.0f}   {tot_EBITDA:,.0f}")

def year_2_to_x_simulation(years,init_revenue,DECIMAL_REV_GROWTH,init_margins,DECIMAL_MARGIN_GROWTH):	
		#margins will not grow beyond 0.25
	def grow_margins(decimal_margins,DECIMAL_MARGIN_GROWTH):
		max_margins = 0.25
		margins = decimal_margins
		margin_growth = DECIMAL_MARGIN_GROWTH 
		new_margins = ( margins + (margins * DECIMAL_MARGIN_GROWTH))

		if new_margins < max_margins:
			return new_margins #returns 0.xx
		else:
			return max_margins #returns 0.25

	revenue = init_revenue
	tot_revenue = revenue
	margins = init_margins
	tot_EBITDA = revenue * init_margins

	for year in range(2,years+1):
		revenue = (revenue + (revenue * DECIMAL_REV_GROWTH) ) 
		margins = grow_margins(margins,DECIMAL_MARGIN_GROWTH)
		EBITDA = revenue * margins
		tot_EBITDA += EBITDA
		
		print(f"{year}  {revenue:,.0f}    {margins*100:.3f}                       {EBITDA:,.0f}   {tot_EBITDA:,.0f}")
		
		#not printed, but must be updated for each year
		tot_revenue += revenue
		final_EBITDA = EBITDA
		
def final_calculations(init_revenue,init_EBITDA,decimal_commission,decimal_interest,sale_EBITDA,years,DECIMAL_REV_GROWTH,init_margins,DECIMAL_MARGIN_GROWTH):

	def year_2_to_x_tot_EBITDA(years,init_revenue,DECIMAL_REV_GROWTH,init_margins,DECIMAL_MARGIN_GROWTH):
		#margins will not grow beyond 0.25
		def grow_margins(decimal_margins,DECIMAL_MARGIN_GROWTH):
			max_margins = 0.25
			margins = decimal_margins
			margin_growth = DECIMAL_MARGIN_GROWTH 
			new_margins = ( margins + (margins * DECIMAL_MARGIN_GROWTH))

			if new_margins < max_margins:
				return new_margins #returns 0.xx
			else:
				return max_margins #returns 0.25

		revenue = init_revenue
		tot_revenue = revenue
		margins = init_margins
		tot_EBITDA = revenue * init_margins

		for year in range(2,years+1):
			revenue = (revenue + (revenue * DECIMAL_REV_GROWTH) ) 
			margins = grow_margins(margins,DECIMAL_MARGIN_GROWTH)
			EBITDA = revenue * margins
			tot_EBITDA += EBITDA
			tot_revenue += revenue
			final_EBITDA = EBITDA

		return tot_EBITDA

	def year_2_to_x_tot_revenue(years,init_revenue,DECIMAL_REV_GROWTH,init_margins,DECIMAL_MARGIN_GROWTH):
		#margins will not grow beyond 0.25
		def grow_margins(decimal_margins,DECIMAL_MARGIN_GROWTH):
			max_margins = 0.25
			margins = decimal_margins
			margin_growth = DECIMAL_MARGIN_GROWTH
			new_margins = ( margins + (margins * DECIMAL_MARGIN_GROWTH))

			if new_margins < max_margins:
				return new_margins #returns 0.xx
			else:
				return max_margins #returns 0.25

		revenue = init_revenue
		tot_revenue = revenue
		margins = init_margins
		tot_EBITDA = revenue * init_margins

		for year in range(2,years+1):
			revenue = (revenue + (revenue * DECIMAL_REV_GROWTH) ) 
			margins = grow_margins(margins,DECIMAL_MARGIN_GROWTH)
			EBITDA = revenue * margins
			tot_EBITDA += EBITDA
			tot_revenue += revenue
			final_EBITDA = EBITDA

		return tot_revenue

	def year_2_to_x_final_EBITDA(years,init_revenue,DECIMAL_REV_GROWTH,init_margins,DECIMAL_MARGIN_GROWTH):
		#margins will not grow beyond 0.25
		def grow_margins(decimal_margins,DECIMAL_MARGIN_GROWTH):
			max_margins = 0.25
			margins = decimal_margins
			margin_growth = DECIMAL_MARGIN_GROWTH 
			new_margins = ( margins + (margins * DECIMAL_MARGIN_GROWTH))

			if new_margins < max_margins:
				return new_margins #returns 0.xx
			else:
				return max_margins #returns 0.25

		revenue = init_revenue
		tot_revenue = revenue
		margins = init_margins
		tot_EBITDA = revenue * init_margins

		for year in range(2,years+1):
			revenue = (revenue + (revenue * DECIMAL_REV_GROWTH) ) 
			margins = grow_margins(margins,DECIMAL_MARGIN_GROWTH)
			EBITDA = revenue * margins
			tot_EBITDA += EBITDA
			tot_revenue += revenue
			final_EBITDA = EBITDA

		return final_EBITDA

	buy_price = init_revenue * init_margins * init_EBITDA
	final_EBITDA = year_2_to_x_final_EBITDA(years,init_revenue,DECIMAL_REV_GROWTH,init_margins,DECIMAL_MARGIN_GROWTH)
	tot_revenue = year_2_to_x_tot_revenue(years,init_revenue,DECIMAL_REV_GROWTH,init_margins,DECIMAL_MARGIN_GROWTH)
	tot_EBITDA = year_2_to_x_tot_EBITDA(years,init_revenue,DECIMAL_REV_GROWTH,init_margins,DECIMAL_MARGIN_GROWTH)
	fee = buy_price * decimal_commission
	interest_payment  = buy_price * decimal_interest
	interest_payments = interest_payment * BOND_DURATION
	profit = (((final_EBITDA * sale_EBITDA) + tot_EBITDA) - (interest_payments + fee + buy_price))
   #perhaps assume profit is spent on improvements?
   #profit = ((final_EBITDA * sale_EBITDA) - (interest_payments + fee))

	print(f"-                        {init_EBITDA}                                      {tot_revenue:,.0f}  {interest_payment:,.0f}/yr+{fee:,.0f}  {sale_EBITDA}  {profit:,.0f}")

def run_simulation(years,init_revenue,DECIMAL_REV_GROWTH,init_margins,DECIMAL_MARGIN_GROWTH,init_EBITDA,decimal_commission,decimal_interest,sale_EBITDA):
	format_header()
	year_one_simulation(init_revenue,init_margins,init_EBITDA)
	year_2_to_x_simulation(years,init_revenue,DECIMAL_REV_GROWTH,init_margins,DECIMAL_MARGIN_GROWTH)
	final_calculations(init_revenue,init_EBITDA,decimal_commission,decimal_interest,sale_EBITDA,years,DECIMAL_REV_GROWTH,init_margins,DECIMAL_MARGIN_GROWTH)

def run_all_simulations():
	count = 0 
	for year in years_list: 
		for init_margin in init_margins_list:
			for sale_x in sale_EBITDA_list:
				for init_x in init_EBITDA_list:
					for com_r in commission_rate_list:
						for interest_r in interest_rate_list:
							for init_rev in init_revenue_list:
								run_simulation(year,init_rev,DECIMAL_REV_GROWTH,init_margin,DECIMAL_MARGIN_GROWTH,init_x,com_r,interest_r,sale_x)
								count += 1
	print(f"# Scenarios: {count:,}")

def run_select_simulations():
	count = 0
	for year in years_list2:
		for init_rev in init_revenue_list:
			for init_margin in init_margins_list2:
				run_simulation(year,init_rev,DECIMAL_REV_GROWTH,init_margin,DECIMAL_MARGIN_GROWTH,4,.1,.09,6)
				count += 1
	print(f"# Scenarios: {count:,}")

def run_key_simulations():
	count = 0
	for year in years_list2:
		for init_margin in init_margins_list2:
			for init_EBITDA in init_EBITDA_list2:
				for sale_EBITDA in sale_EBITDA_list2:
					run_simulation(year,1000000,DECIMAL_REV_GROWTH,init_margin,DECIMAL_MARGIN_GROWTH,init_EBITDA,.1,0.09,5)
					count += 1
	print(f"# Scenarios: {count:,}")

init_margins_list2    = [.16,.18,.20,.25]
init_revenue_list2    = [1000000]
commission_rate_list2 = [0.10]
interest_rate_list2   = [0.07,0.08,0.09]
years_list2           = [5]
init_EBITDA_list2     = [4,5,6]
sale_EBITDA_list2     = [5,6,7,10]

#run_select_simulations()
#run_key_simulations()

run_simulation(5,5000000,DECIMAL_REV_GROWTH,0.18,DECIMAL_MARGIN_GROWTH,5,0.1,0.09,5)

