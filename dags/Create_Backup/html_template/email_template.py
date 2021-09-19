"""
Author:Sony Shrestha
Description: This progarm defines template for sending mail
Date: 27 September, 2020
"""


global salutation

global success_title
global success_body

global failure_title
global failure_body

global regards



salutation="""Respected Sir/Madam,
"""


success_title="""passed"""

success_body="""Above task has been successfully executed.
"""

failure_title="""failed"""

failure_body="""Above task failed to execute. Find attached log file to debug error for respective task.
"""

regards="""Thank you.
<br>
<br>
With regards,
<br>
Airflow Automated Mail
"""
