#!/usr/bin/env python3# -*- coding: utf-8 -*-"""Created on 2017/6/2 下午6:11@author: zhechengma"""import pandas as pdfrom pandas import DataFrame,Seriesfrom input import connectDatabasefrom output_setting import *dcd=connectDatabase()#from c_base_info import c_basec_base_info_df=DataFrame(dcd.select(c_base_info))c_base_info_df.to_sql(c_base_info,con = engine,if_exists = 'append',index = False,index_label = True)#from c_alter_info import c_alter_infoc_alter_info_df=dcd.select(c_alter_info)c_alter_info_df.to_sql(c_alter_info,con=engine,if_exists = 'append',index = False,index_label = True)#from c_branch_info import c_branch_info# c_branch__info_df=dcd.select(c_branch_info)# c_branch__info_df.to_sql(c_branch_info,con=engine,if_exists = 'append',index = False,index_label = True)#from c_cashflow_infoc_cashflow_info_df=dcd.select(c_cashflow_info)c_cashflow_info_df.to_sql(c_cashflow_info,con = engine,if_exists = 'append',index = False,index_label = True)#c_holder_infoc_holder_info_df=dcd.select(c_holder_info)c_holder_info_df.to_sql(c_holder_info,con = engine,if_exists = 'append',index = False,index_label = True)#c_investion_infoc_investion_info_df=dcd.select(c_investion_info)c_investion_info_df.to_sql(c_investion_info,con = engine,if_exists = 'append',index = False,index_label = True)#c_keyPerson_infoc_keyperson_info_df=dcd.select(c_keyperson_info)c_keyperson_info_df.to_sql('c_keyperson_info',con = engine,if_exists = 'append',index = False,index_label = True)#c_procfic_infoc_profic_info_df=dcd.select(c_profic_info)c_profic_info_df.to_sql(c_profic_info,con = engine,if_exists = 'append',index = False,index_label = True)