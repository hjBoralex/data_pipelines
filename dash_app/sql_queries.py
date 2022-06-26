# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 16:45:57 2022

@author: hermann.ngayap
"""
#Sql queries to pull out data from the sql server DB
import pandas as pd
import pyodbc
import sqlalchemy
from sqlalchemy import create_engine
from server_credentials import server_credentials

def open_database():
    print('Connecting to SQL Server with ODBC driver')
    connection_string = 'DRIVER={SQL Server};SERVER='+server_credentials['server']+';DATABASE='+server_credentials['database']+';UID='+server_credentials['username']+';Trusted_Connection='+server_credentials['yes']
    cnxn = pyodbc.connect(connection_string)
    print('connected!')

    return cnxn

#windows authentication 
def mssql_engine(): 
    engine = create_engine('mssql+pyodbc://BLX186-SQ1PRO01/StarDust?driver=SQL+Server+Native+Client+11.0') 
    return engine
#================================================================
#======================= SQL Queries  ===========================
#================================================================
#======1. Exposition per year

query_1 ="SELECT année, ROUND(ISNULL(SUM(p50), 0)/1000, 5) + (SELECT ROUND(ISNULL(SUM(p50), 0)/1000,5) \
												FROM p50_p90_hedge AS h  \
												WHERE a.année=h.année) AS yearly_exposition \
FROM p50_p90_asset AS a \
GROUP BY année \
ORDER BY année";
query_results_1 = pd.read_sql(query_1, mssql_engine()) 

#======2. Exposition per quarter per year

query_2 ="SELECT année, trimestre, \
                  CASE WHEN LEFT(trimestre, 2)='Q1' THEN 'Q1' \
                       WHEN LEFT(trimestre, 2)='Q2' THEN 'Q2' \
                       WHEN LEFT(trimestre, 2)='Q3' THEN 'Q3' \
                       WHEN LEFT(trimestre, 2)='Q4' THEN 'Q4' \
                       END AS quarters, \
          ROUND(ISNULL(SUM(p50), 0)/1000, 5) + (SELECT ROUND(ISNULL(SUM(p50), 0)/1000, 5) \
												FROM p50_p90_hedge AS h  \
												WHERE a.année=h.année AND a.trimestre=h.trimestre) AS quarterly_exposition \
FROM p50_p90_asset AS a \
GROUP BY année, trimestre \
ORDER BY année, trimestre";
query_results_2 = pd.read_sql(query_2, mssql_engine())

#======3. Exposition per month per year

query_3="SELECT année, mois, \
        CASE WHEN mois=1 THEN 'jan'\
            WHEN mois=2 THEN 'feb' \
            WHEN mois=3 THEN 'mar' \
            WHEN mois=4 THEN 'apr' \
            WHEN mois=5 THEN 'may' \
            WHEN mois=6 THEN 'jun' \
            WHEN mois=7 THEN 'jul' \
            WHEN mois=8 THEN 'aug' \
            WHEN mois=9 THEN 'sep' \
            WHEN mois=10 THEN 'oct' \
            WHEN mois=11 THEN 'nov' \
            WHEN mois=12 THEN 'dec' \
        END AS months,\
        ROUND(ISNULL(SUM(p50), 0)/1000, 5) + (SELECT ROUND(ISNULL(SUM(p50), 0)/1000, 5) \
					  FROM p50_p90_hedge AS h \
					  WHERE a.année=h.année AND a.mois=h.mois) AS monthly_exposition \
FROM p50_p90_asset AS a \
GROUP BY année, mois \
ORDER BY année, mois;"
query_results_3 = pd.read_sql(query_3, mssql_engine())

#=====4. Hedge type per year

query_4 ="SELECT année, \
                 CASE WHEN type_hedge = 'CR16' THEN 'CR' \
                      WHEN type_hedge = 'CR17' THEN 'CR' \
                      WHEN type_hedge = 'CR' THEN 'CR' \
                      WHEN type_hedge = 'OA' THEN 'OA' \
                      WHEN type_hedge = 'PPA' THEN 'PPA' \
                 END AS type_contract, \
                ROUND(ISNULL(SUM(-p50), 0)/1000, 5) AS hedge \
          FROM p50_p90_hedge \
          GROUP BY année, \
              CASE WHEN type_hedge='CR16' THEN 'CR' \
                   WHEN type_hedge='CR17' THEN 'CR' \
                   WHEN type_hedge='CR' THEN 'CR' \
                   WHEN type_hedge='OA' THEN 'OA' \
                   WHEN type_hedge='PPA' THEN 'PPA' \
              END \
          ORDER BY année, type_contract;"
query_results_4 = pd.read_sql(query_4, mssql_engine())  
  
#=====5. Hedge per quarter per year

query_5 ="SELECT année, trimestre, \
                 CASE WHEN type_hedge = 'CR16' THEN 'CR' \
                      WHEN type_hedge = 'CR17' THEN 'CR' \
                      WHEN type_hedge = 'CR' THEN 'CR' \
                      WHEN type_hedge = 'OA' THEN 'OA' \
                      WHEN type_hedge = 'PPA' THEN 'PPA' \
                 END AS type_contract, \
                 CASE WHEN LEFT(trimestre, 2)='Q1' THEN 'Q1' \
                      WHEN LEFT(trimestre, 2)='Q2' THEN 'Q2' \
                      WHEN LEFT(trimestre, 2)='Q3' THEN 'Q3' \
                      WHEN LEFT(trimestre, 2)='Q4' THEN 'Q4' \
                      END AS quarters, \
                ROUND(ISNULL(SUM(-p50), 0)/1000, 5) AS hedge \
          FROM p50_p90_hedge \
          GROUP BY année, trimestre, \
              CASE WHEN type_hedge='CR16' THEN 'CR' \
                   WHEN type_hedge='CR17' THEN 'CR' \
                   WHEN type_hedge='CR' THEN 'CR' \
                   WHEN type_hedge='OA' THEN 'OA' \
                   WHEN type_hedge='PPA' THEN 'PPA' \
                   END \
          ORDER BY année, quarters;"
query_results_5 = pd.read_sql(query_5, mssql_engine())  

#=====6. Hedge per month per year
query_6 ="SELECT année, mois,\
                 CASE WHEN type_hedge = 'CR16' THEN 'CR' \
                      WHEN type_hedge = 'CR17' THEN 'CR' \
                      WHEN type_hedge = 'CR' THEN 'CR' \
                      WHEN type_hedge = 'OA' THEN 'OA' \
                      WHEN type_hedge = 'PPA' THEN 'PPA' \
                 END AS type_contract, \
                 CASE WHEN mois=1 THEN 'jan'\
                      WHEN mois=2 THEN 'feb' \
                      WHEN mois=3 THEN 'mar' \
                      WHEN mois=4 THEN 'apr' \
                      WHEN mois=5 THEN 'may' \
                      WHEN mois=6 THEN 'jun' \
                      WHEN mois=7 THEN 'jul' \
                      WHEN mois=8 THEN 'aug' \
                      WHEN mois=9 THEN 'sep' \
                      WHEN mois=10 THEN 'oct' \
                      WHEN mois=11 THEN 'nov' \
                      WHEN mois=12 THEN 'dec' \
                 END AS months,\
                ROUND(ISNULL(SUM(-p50), 0)/1000, 5) AS hedge \
          FROM p50_p90_hedge \
          GROUP BY année, mois,\
              CASE WHEN type_hedge='CR16' THEN 'CR' \
                   WHEN type_hedge='CR17' THEN 'CR' \
                   WHEN type_hedge='CR' THEN 'CR' \
                   WHEN type_hedge='OA' THEN 'OA' \
                   WHEN type_hedge='PPA' THEN 'PPA' \
                   END \
          ORDER BY année, mois;"
query_results_6 = pd.read_sql(query_6, mssql_engine()) 

#=====7.HCR per year
query_7 = "SELECT année, ROUND((SELECT ISNULL(SUM(-p50), 0) \
                        FROM p50_p90_hedge AS h \
                        WHERE a.année=h.année) / ISNULL(SUM(p50), 0), 2) AS HCR_per_year \
            FROM p50_p90_asset AS a \
            GROUP BY année \
            ORDER BY année;"
query_results_7 = pd.read_sql(query_7, mssql_engine())
#=====8.HCR per quarter
query_8 = "SELECT année, trimestre, \
                  CASE WHEN LEFT(trimestre, 2) = 'Q1' THEN 'Q1' \
                       WHEN LEFT(trimestre, 2) = 'Q2' THEN 'Q2' \
                       WHEN LEFT(trimestre, 2) = 'Q3' THEN 'Q3' \
                       WHEN LEFT(trimestre, 2) = 'Q4' THEN 'Q4' \
                       END AS quarters,\
                           (SELECT ISNULL(SUM(-p50), 0) \
                            FROM p50_p90_hedge AS h \
                            WHERE a.année=h.année AND  a.trimestre=h.trimestre) / ISNULL(SUM(p50), 0) AS HCR_per_quarter \
            FROM p50_p90_asset AS a \
            GROUP BY année, trimestre \
            ORDER BY année, trimestre;"
query_results_8= pd.read_sql(query_8, mssql_engine())
#=====9.HCR per month
query_9 = "SELECT année, mois, (SELECT ISNULL(SUM(-p50), 0) \
                        FROM p50_p90_hedge AS h \
                        WHERE a.année=h.année AND  a.mois=h.mois) / ISNULL(SUM(p50), 0) AS HCR_per_quarter \
            FROM p50_p90_asset AS a \
            GROUP BY année, mois \
            ORDER BY année, mois;"
query_results_9= pd.read_sql(query_9, mssql_engine())


#=============================
#====    PRODUCTION  =========
#=============================

#=====Prod per year

query_10 = "SELECT année, \
                   ROUND(ISNULL(SUM(p50), 0)/1000, 5) AS prod_per_year \
            FROM p50_p90_asset AS a \
            GROUP BY année \
            ORDER BY année;"
query_results_10 = pd.read_sql(query_10, mssql_engine())

#====Prod per quarter

query_11 = "SELECT année, trimestre, \
                   CASE WHEN LEFT(trimestre, 2)='Q1' THEN 'Q1' \
                   WHEN LEFT(trimestre, 2)='Q2' THEN 'Q2' \
                   WHEN LEFT(trimestre, 2)='Q3' THEN 'Q3' \
                   WHEN LEFT(trimestre, 2)='Q4' THEN 'Q4' \
                   END AS quarters, \
                   ROUND(ISNULL(SUM(p50), 0)/1000, 5) AS prod_per_quarter \
            FROM p50_p90_asset \
            GROUP BY année, trimestre \
            ORDER BY année, trimestre;"
query_results_11 = pd.read_sql(query_11, mssql_engine())            

#=====Prod per month
query_12 = "SELECT année, mois, \
                   CASE WHEN mois=1 THEN 'jan' \
                        WHEN mois=2 THEN 'feb' \
                        WHEN mois=3 THEN 'mar' \
	                    WHEN mois=4 THEN 'apr' \
			            WHEN mois=5 THEN 'may' \
			            WHEN mois=6 THEN 'jun' \
			            WHEN mois=7 THEN 'jul' \
			            WHEN mois=8 THEN 'aug' \
			            WHEN mois=9 THEN 'sep' \
			            WHEN mois=10 THEN 'oct' \
			            WHEN mois=11 THEN 'nov' \
			            WHEN mois=12 THEN 'dec' \
			       END AS months, \
ROUND(ISNULL(SUM(p50), 0)/1000, 5) AS prod_per_month \
FROM p50_p90_asset \
GROUP BY année, mois \
ORDER BY année, mois;"
query_results_12 = pd.read_sql(query_12, mssql_engine())   

#=====Fixed & merchant per year
query_13 = "SELECT année, \
            SUM(CASE WHEN type_hedge='CR16' OR type_hedge='CR17' OR type_hedge='CR' OR type_hedge='OA' THEN -p50/1000 END) AS fixed_price, \
			SUM(CASE WHEN type_hedge='PPA' THEN  -p50/1000 END) AS merchant \
FROM p50_p90_hedge \
GROUP BY année \
ORDER BY année;"
query_results_13 = pd.read_sql(query_13, mssql_engine())

#=====Fixed & merchant per quarter
query_14 = "SELECT année, trimestre, \
			CASE WHEN LEFT(trimestre, 2)='Q1' THEN 'Q1' \
			WHEN LEFT(trimestre, 2)='Q2' THEN 'Q2' \
			WHEN LEFT(trimestre, 2)='Q3' THEN 'Q3' \
			WHEN LEFT(trimestre, 2)='Q4' THEN 'Q4' \
			END AS quarters, \
			SUM(CASE WHEN type_hedge='CR16' OR type_hedge='CR17' OR type_hedge='CR' OR type_hedge='OA' THEN -p50/1000 END) AS fixed_price, \
			SUM(CASE WHEN type_hedge='PPA' THEN  -p50/1000 END) AS merchant \
FROM p50_p90_hedge \
GROUP BY année, trimestre \
ORDER BY année, trimestre;"
query_results_14 = pd.read_sql(query_14, mssql_engine())

#=====Fixed & merchant per months
query_15 = "SELECT année, mois, \
		CASE WHEN mois=1 THEN 'jan' \
			 WHEN mois=2 THEN 'feb' \
			 WHEN mois=3 THEN 'mar' \
	         WHEN mois=4 THEN 'apr' \
			 WHEN mois=5 THEN 'may' \
			 WHEN mois=6 THEN 'jun' \
			 WHEN mois=7 THEN 'jul' \
			 WHEN mois=8 THEN 'aug' \
			 WHEN mois=9 THEN 'sep' \
			 WHEN mois=10 THEN 'oct' \
			 WHEN mois=11 THEN 'nov' \
			 WHEN mois=12 THEN 'dec' \
		END AS months, \
			SUM(CASE WHEN type_hedge='CR16' OR type_hedge='CR17' OR type_hedge='CR' OR type_hedge='OA' THEN -p50/1000 END) AS fixed_price, \
			SUM(CASE WHEN type_hedge='PPA' THEN  -p50/1000 END) AS merchant \
FROM p50_p90_hedge \
GROUP BY année, mois \
ORDER BY année, mois;"
query_results_15 = pd.read_sql(query_15, mssql_engine())
#=====PPA fixed exp per year
query_16 = "SELECT année, \
                    SUM(CASE WHEN type_hedge='PPA' THEN  -p50/1000 END) AS ppa_fixed  \
                        FROM p50_p90_hedge \
                        GROUP BY année \
                        ORDER BY année;"
query_results_16 = pd.read_sql(query_16, mssql_engine())