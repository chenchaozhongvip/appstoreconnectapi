#!/usr/bin/env python

import sys
from appstoreconnect import Api


if __name__ == "__main__":
	key_id = sys.argv[1] # 479L849VK2
	key_file = sys.argv[2]
	issuer_id = sys.argv[3] # 69b7a93b-1e01-4c97-959f-e124571c5fbd
	api = Api(key_id, key_file, issuer_id)

	# list all apps
	# apps = api.list_devices()
	# for app in apps:
	# 	print(app.name, app.udid)
	apps = api.list_apps()
	for app in apps:
		print(app.name, app.sku)
	# filter apps
	# apps = api.list_apps(filters={'sku': 'DINORUSH', 'name': 'Dino Rush'})
	# print("%d apps found" % len(apps))

	# # download sales report
	# api.download_sales_and_trends_reports(
	# 	filters={'vendorNumber': '123456789', 'frequency': 'WEEKLY', 'reportDate': '2019-06-09'}, save_to='report.csv')

	# # download finance report
	# api.download_finance_reports(filters={'vendorNumber': '123456789', 'reportDate': '2019-06'}, save_to='finance.csv')

