#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Savings

def savings(gross_pay, tax_rate, expenses):
    
    output = (float(tax_rate) * int(gross_pay)) - int(expenses)

    return output


# In[4]:


# Material Waste

def material_waste(total_material, material_units, num_jobs, job_consumption):
    
    computation = int(total_material) - (int(num_jobs) * int(job_consumption))
    output = str(computation) + str(material_units)
 
    return output


# In[1]:


# Interest

def interest(principal, rate, periods):
    
    interest = int(principal) * (float(rate) * int(periods))
    output = int(principal) + int(interest)

    return output


# In[2]:


# Body Mass Index

def body_mass_index(weight, height):
    
    weight_metric = float(weight) * 0.453592
    height_metric = (float(height[0]) * 0.3048) + (float(height[1]) * 0.0254)
    output = float(weight_metric) / (float(height_metric) ** 2)

    return output

