SELECT DISTINCT date_id, make_name, COUNT(DISTINCT lead_id) as 
unique_leads, COUNT(DISTINCT partner_id) as unique_partners
FROM dailySales
GROUP BY date_id, make_name