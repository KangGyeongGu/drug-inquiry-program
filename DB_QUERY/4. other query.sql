SELECT D.DRUGBANK_ID, D.NAME AS DRUG_NAME, P.SMPDB_ID, P.NAME AS PATHWAY_NAME, P.CATEGORY AS PATHWAY_CATEGORY
FROM DRUG D
JOIN DRUG_PATH_ASSOCIATION DPA ON D.DRUGBANK_ID = DPA.DRUGBANK_ID
JOIN PATHWAY P ON DPA.SMPDB_ID = P.SMPDB_ID;


SELECT D.DRUGBANK_ID, D.NAME AS DRUG_NAME, E.ENZYME_ID, E.NAME AS ENZYME_NAME, DEA.ENZYME_ACTION
FROM DRUG D
JOIN DRUG_ENZYME_ACTION DEA ON D.DRUGBANK_ID = DEA.DRUGBANK_ID
JOIN ENZYME E ON DEA.ENZYME_ID = E.ENZYME_ID;


UPDATE CLASSIFICATION
SET KINGDOM = NULL
WHERE DRUGBANK_ID = 'DB00001';

SELECT * FROM CLASSIFICATION WHERE DRUGBANK_ID = 'DB00001';
