# gv.at Domain List

Sanitized list of Austrian government domains with TLS

# Usage

Open [domainlist.html](domainlist.html) in your browser.

# Updating

1. Connect to crt.sh with psql
   `psql -h crt.sh -p 5432 -U guest certwatch`

2. Dump the results to CSV
   `\copy (SELECT ci.ISSUER_CA_ID, ca.NAME ISSUER_NAME, ci.NAME_VALUE NAME_VALUE, min(c.ID) MIN_CERT_ID, min(ctle.ENTRY_TIMESTAMP) MIN_ENTRY_TIMESTAMP, x509_notBefore(c.CERTIFICATE) NOT_BEFORE FROM ca, ct_log_entry ctle, certificate_identity ci, certificate c WHERE ci.ISSUER_CA_ID = ca.ID AND c.ID = ctle.CERTIFICATE_ID AND reverse(lower(ci.NAME_VALUE)) LIKE reverse(lower('%.gv.at')) AND ci.CERTIFICATE_ID = c.ID GROUP BY c.ID, ci.ISSUER_CA_ID, ISSUER_NAME, NAME_VALUE ORDER BY MIN_ENTRY_TIMESTAMP DESC, NAME_VALUE, ISSUER_NAME) TO 'gv.at.csv' CSV HEADER`

3. Run script
   `python3 domains.py`

# License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
