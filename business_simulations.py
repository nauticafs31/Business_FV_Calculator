#import csv
#import os
import math

# these constants will be used for any and all "scenarios" you decide to run on the build
DECIMAL_MARGIN_GROWTH = 0.000000005
DECIMAL_REV_GROWTH    = 0.02
BOND_DURATION = 5

# these lists contain variants for each key metric. 
years_list             = [3      , 5      , 7      , 10 ]
init_margins_list      = [0.16   , 0.18   , 0.2    , 0.22]
sale_EBITDA_list       = [5      , 6      , 7      , 10 ]
init_EBITDA_list            = [4      , 5      , 6      ]
commission_rate_list        = [0.1    , 0.12   , 0.15   ]
interest_rate_list          = [0.07   , 0.08   , 0.09   ]
init_revenue_list           = [1000000, 1500000, 2000000]

# a second set of lists, containing fewer potential metrics, and therefore fewer potential combinations of metrics
years_list2           = [5]
init_margins_list2    = [.16,.18,.20,.25]
init_EBITDA_list2     = [4,5,6]
sale_EBITDA_list2     = [5,6,7,10]
commission_rate_list2 = [0.10]
interest_rate_list2   = [0.07,0.08,0.09]
init_revenue_list2    = [1000000]


# formats the header that will output to the console
def format_header():
	print("---------------------------------------------------------------------------------------------------------")
	print("YR  REVENUE    MARGINS  xBUY   BUY PRICE    YR.EBITDA  TOT.EB.   TOT.REV.    INTEREST/FEES  xSALE  PROFIT")

	
# every year, it is assumed that the margins compound upon the previous year. This function ensures growth in compounded, not linear
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
	
	
# year one of the simulation is unique regarding initial values. This function sets the variables to those provided as parameters
def year_one_simulation(init_revenue,init_margins,init_EBITDA):	
	revenue = init_revenue
	margins = init_margins #0.xx
	buy_price = init_revenue * init_margins * init_EBITDA

	EBITDA = revenue * init_margins
 
	tot_EBITDA = EBITDA	
	tot_revenue = revenue

	print(f"1  {revenue:,.0f}    {margins*100:.3f}           {buy_price:,.0f}     {EBITDA:,.0f}   {tot_EBITDA:,.0f}")

	
# function that calculates and prints the relevant metrics to the console, for each year corresponind to the lifespan of the simulation
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

		
# at the end of the simulation, some important metrics are outputted to the console. A sort of summary if you will.
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

	
# this function ties together all the above, and finally produces a valuable output
def run_simulation(years,init_revenue,DECIMAL_REV_GROWTH,init_margins,DECIMAL_MARGIN_GROWTH,init_EBITDA,decimal_commission,decimal_interest,sale_EBITDA):
	format_header()
	year_one_simulation(init_revenue,init_margins,init_EBITDA)
	year_2_to_x_simulation(years,init_revenue,DECIMAL_REV_GROWTH,init_margins,DECIMAL_MARGIN_GROWTH)
	final_calculations(init_revenue,init_EBITDA,decimal_commission,decimal_interest,sale_EBITDA,years,DECIMAL_REV_GROWTH,init_margins,DECIMAL_MARGIN_GROWTH)

	
# for each variable in the first group of lists above, a scenario is simulated (and output to the console)
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

	
# runs based on the second group of list at top of script. Will result in fewer scenarios being simulated.
# feel free to add nested loops from that second list, not all variables are currently being used (for sake of fewer outputs)
def run_select_simulations():
	count = 0
	for year in years_list2:
		for init_rev in init_revenue_list2:
			for init_margin in init_margins_list2:
				run_simulation(year,init_rev,DECIMAL_REV_GROWTH,init_margin,DECIMAL_MARGIN_GROWTH,4,.1,.09,6)
				count += 1
	print(f"# Scenarios: {count:,}")

	

#run_all_simulations()
#run_select_simulations()

# this function requires all variables to be input manually. It will run only one scenario.
run_simulation(5,5000000,DECIMAL_REV_GROWTH,0.18,DECIMAL_MARGIN_GROWTH,5,0.1,0.09,5)

