INSERT INTO DRUG (DRUGBANK_ID, NAME, DESCRIPTION, CAS_NUMBER) 
VALUES 
('DB00001', 'Lepirudin', 'Lepirudin is a recombinant hirudin formed by 65 amino acids that acts as a highly specific and direct thrombin inhibitor. Natural hirudin is an endogenous anticoagulant found in Hirudo medicinalis leeches. Lepirudin is produced in yeast cells and is identical to natural hirudin except for the absence of sulfate on the tyrosine residue at position 63 and the substitution of leucine for isoleucine at position 1 (N-terminal end). Lepirudin is used as an anticoagulant in patients with heparin-induced thrombocytopenia (HIT), an immune reaction associated with a high risk of thromboembolic complications.', '138068-37-8'),
('DB00002', 'Cetuximab', 'Cetuximab is a recombinant chimeric human/mouse IgG1 monoclonal antibody that competitively binds to epidermal growth factor receptor (EGFR) and competitively inhibits the binding of epidermal growth factor (EGF). EGFR is a member of the ErbB family of receptor tyrosine kinases found in both normal and tumour cells; it is responsible for regulating epithelial tissue development and homeostasis. EGFR has been implicated in various types of cancer, as it is often overexpressed in malignant cells and EGFR overexpression has been linked to more advanced disease and poor prognosis. Cetuximab is used for the treatment of head and neck cancer and metastatic, KRAS wild-type colorectal cancer, and metastatic colorectal cancer with a BRAF V600E mutation.', '205923-56-4'),
('DB00003', 'Dornase alfa', 'Dornase alfa is a biosynthetic form of human deoxyribonuclease I (DNase I) enzyme. It is produced in genetically modified Chinese hamster ovary (CHO) cells using recombinant DNA technology. The 260-amino acid sequence of dornase alfa is identical to the endogenous human enzyme. Dornase alfa cleaves extracellular DNA to 5-phosphodinucleotide and 5-phosphooligonucleotide end products without affecting intracellular DNA. It is used to reduce sputum viscosity in individuals with cystic fibrosis.', '143831-71-4'),
('DB00004', 'Denileukin diftitox', 'Denileukin diftitox is a recombinant DNA-derived cytotoxic protein composed of the amino acid sequences for diphtheria toxin fragments A and B (Met 1-Thr 387)-His followed by the sequences for interleukin-2 (IL-2; Ala 1-Thr 133).', '173146-27-5'),
('DB00005', 'Etanercept', 'Etanercept is a dimeric fusion protein consisting of the extracellular ligand-binding portion of the human 75 kilodalton (p75) tumor necrosis factor receptor (TNFR) linked to the Fc portion of human IgG1. It is used to treat or manage a variety of inflammatory conditions including rheumatoid arthritis (RA), ankylosing spondylitis (AS), and juvenile idiopathic poly-articular arthritis (JIA).', '185243-69-0'),
('DB00006', 'Bivalirudin', 'Bivalirudin is a synthetic 20 residue peptide (thrombin inhibitor) which reversibly inhibits thrombin. Once bound to the active site, thrombin cannot activate fibrinogen into fibrin, the crucial step in the formation of thrombus. It is administered intravenously and is used in anticoagulation therapies.', '128270-60-0'),
('DB00007', 'Leuprolide', 'Leuprolide is a synthetic 9-residue peptide analogue of gonadotropin-releasing hormone (GnRH). Leuprolide binds to the GnRH receptor, leading to modulation of gonadotropin hormone and sex steroid levels. It is used for the treatment of advanced prostate cancer, endometriosis, and central precocious puberty.', '53714-56-0'),
('DB00008', 'Peginterferon alfa-2a', 'Peginterferon alfa-2a is a form of recombinant interferon used as part of combination therapy to treat chronic Hepatitis C. It is derived from recombinant human interferon and induces the body’s innate antiviral response by activating the JAK/STAT pathway.', '198153-51-4'),
('DB00009', 'Alteplase', 'Alteplase is a recombinant tissue plasminogen activator (rt-PA) used as a thrombolytic agent. It cleaves plasminogen to form plasmin, which breaks down fibrin clots. It is used in the management of thromboembolic diseases, including acute myocardial infarction and ischemic stroke.', '105857-23-6'),
('DB00010', 'Sermorelin', 'Sermorelin acetate is the acetate salt of an amidated synthetic 29-amino acid peptide that corresponds to the amino-terminal segment of human growth hormone-releasing hormone (GHRH). It is used to stimulate growth hormone production in children and adults with growth hormone deficiencies.', '86168-78-7');


INSERT INTO classification (drugbank_id, kingdom, superclass, class, subclass) 
VALUES
('DB00001', 'Organic Compounds', 'Organic Acids', 'Carboxylic Acids and Derivatives', 'Amino Acids, Peptides, and Analogues'),
('DB00002', 'Organic Compounds', 'Organic Acids', 'Carboxylic Acids and Derivatives', 'Amino Acids, Peptides, and Analogues'),
('DB00003', 'Organic Compounds', 'Organic Acids', 'Carboxylic Acids and Derivatives', 'Amino Acids, Peptides, and Analogues'),
('DB00005', 'Organic Compounds', 'Organic Acids', 'Carboxylic Acids and Derivatives', 'Amino Acids, Peptides, and Analogues'),
('DB00006', 'Organic Compounds', 'Organic Polymers', 'Polypeptides', NULL),
('DB00008', 'Organic Compounds', 'Organic Acids', 'Carboxylic Acids and Derivatives', 'Amino Acids, Peptides, and Analogues'),
('DB00009', 'Organic Compounds', 'Organic Acids', 'Carboxylic Acids and Derivatives', 'Amino Acids, Peptides, and Analogues'),
('DB00010', 'Organic Compounds', 'Organic Acids', 'Carboxylic Acids and Derivatives', 'Amino Acids, Peptides, and Analogues');


INSERT INTO target (target_id, name, organism)
VALUES
('BE0000048', 'Prothrombin', 'Humans'),
('BE0000767', 'Epidermal growth factor receptor', 'Humans'),
('BE0000901', 'Low affinity immunoglobulin gamma Fc region receptor III-B', 'Humans'),
('BE0002094', 'Complement C1q subcomponent subunit A', 'Humans'),
('BE0002095', 'Complement C1q subcomponent subunit B', 'Humans'),
('BE0002096', 'Complement C1q subcomponent subunit C', 'Humans'),
('BE0002097', 'Low affinity immunoglobulin gamma Fc region receptor III-A', 'Humans'),
('BE0000710', 'High affinity immunoglobulin gamma Fc receptor I', 'Humans'),
('BE0002098', 'Low affinity immunoglobulin gamma Fc region receptor II-a', 'Humans'),
('BE0004796', 'DNA', 'Humans'),
('BE0000658', 'Interleukin-2 receptor subunit alpha', 'Humans'),
('BE0000651', 'Interleukin-2 receptor subunit beta', 'Humans'),
('BE0002102', 'Cytokine receptor common subunit gamma', 'Humans'),
('BE0000704', 'Tumor necrosis factor', 'Humans'),
('BE0001087', 'Lymphotoxin-alpha', 'Humans'),
('BE0002099', 'Low affinity immunoglobulin gamma Fc region receptor II-b', 'Humans'),
('BE0002100', 'Low affinity immunoglobulin gamma Fc region receptor II-c', 'Humans'),
('BE0009995', 'Complement component 1q (C1q)', 'Humans'),
('BE0000203', 'Gonadotropin-releasing hormone receptor', 'Humans'),
('BE0000385', 'Interferon alpha/beta receptor 2', 'Humans'),
('BE0000661', 'Interferon alpha/beta receptor 1', 'Humans'),
('BE0000211', 'Plasminogen', 'Humans'),
('BE0000538', 'Fibrinogen alpha chain', 'Humans'),
('BE0002092', 'Fibrinogen gamma chain', 'Humans'),
('BE0000240', 'Plasminogen activator inhibitor 1', 'Humans'),
('BE0000625', 'Growth hormone-releasing hormone receptor', 'Humans');


INSERT INTO drug_target (drugbank_id, target_id) 
VALUES
('DB00001', 'BE0000048'),
('DB00002', 'BE0000767'),
('DB00002', 'BE0000901'),
('DB00002', 'BE0002094'),
('DB00002', 'BE0002095'),
('DB00002', 'BE0002096'),
('DB00002', 'BE0002097'),
('DB00002', 'BE0000710'),
('DB00002', 'BE0002098'),
('DB00003', 'BE0004796'),
('DB00004', 'BE0000658'),
('DB00004', 'BE0000651'),
('DB00004', 'BE0002102'),
('DB00005', 'BE0000704'),
('DB00005', 'BE0001087'),
('DB00005', 'BE0000710'),
('DB00005', 'BE0002098'),
('DB00005', 'BE0002099'),
('DB00005', 'BE0002100'),
('DB00005', 'BE0002097'),
('DB00005', 'BE0000901'),
('DB00005', 'BE0009995'),
('DB00006', 'BE0000048'),
('DB00007', 'BE0000203'),
('DB00008', 'BE0000385'),
('DB00008', 'BE0000661'),
('DB00009', 'BE0000211'),
('DB00009', 'BE0000538'),
('DB00009', 'BE0002092'),
('DB00009', 'BE0000240'),
('DB00010', 'BE0000625');

INSERT INTO enzyme (enzyme_id, name, organism)
VALUES
('BE0001075', 'Myeloperoxidase', 'Humans'),
('BE0002433', 'Cytochrome P450 1A2', 'Humans'),
('BE0001198', 'Macrophage metalloelastase', 'Humans'),
('BE0000394', 'Neutrophil elastase', 'Humans'),
('BE0002363', 'Cytochrome P450 2D6', 'Humans'),
('BE0002793', 'Cytochrome P450 2C9', 'Humans'),
('BE0000048', 'Prothrombin', 'Humans'),
('BE0000380', 'Vitamin K-dependent protein C', 'Humans'),
('BE0001183', 'Insulin-degrading enzyme', 'Humans'),
('BE0002124', 'Neuroendocrine convertase 2', 'Humans'),
('BE0002125', 'Neuroendocrine convertase 1', 'Humans'),
('BE0000262', 'Prostaglandin G/H synthase 2', 'Humans'),
('BE0000017', 'Prostaglandin G/H synthase 1', 'Humans');


INSERT INTO drug_enzyme_action (drugbank_id, enzyme_id, enzyme_action)
VALUES
('DB00006', 'BE0001075', 'inhibitor'),
('DB00008', 'BE0002433', 'inhibitor');


INSERT INTO pathway (smpdb_id, name, category)
VALUES
('SMP0000278', 'Lepirudin Action Pathway', 'drug_action'),
('SMP0000474', 'Cetuximab Action Pathway', 'drug_action'),
('SMP0000277', 'Bivalirudin Action Pathway', 'drug_action'),
('SMP0000280', 'Alteplase Action Pathway', 'drug_action'),
('SMP0000284', 'Urokinase Action Pathway', 'drug_action'),
('SMP0000285', 'Reteplase Action Pathway', 'drug_action'),
('SMP0000281', 'Anistreplase Action Pathway', 'drug_action'),
('SMP0000283', 'Tenecteplase Action Pathway', 'drug_action'),
('SMP0000265', 'Abciximab Action Pathway', 'drug_action'),
('SMP0000266', 'Eptifibatide Action Pathway', 'drug_action'),
('SMP0000476', 'Trastuzumab Action Pathway', 'drug_action'),
('SMP0000282', 'Streptokinase Action Pathway', 'drug_action'),
('SMP0000420', 'Bevacizumab Action Pathway', 'drug_action'),
('SMP0000002', 'Carbamoyl Phosphate Synthetase Deficiency', 'disease');


INSERT INTO DRUG_PATH_ASSOCIATION (DRUGBANK_ID, SMPDB_ID, UNIPROT_ID) VALUES
('DB00001', 'SMP0000278', 'P00734'),
('DB00001', 'SMP0000278', 'P00748'),
('DB00001', 'SMP0000278', 'P02452'),
('DB00001', 'SMP0000278', 'P03952'),
('DB00001', 'SMP0000278', 'P03951'),
('DB00001', 'SMP0000278', 'P00740'),
('DB00001', 'SMP0000278', 'P00451'),
('DB00001', 'SMP0000278', 'P12259'),
('DB00001', 'SMP0000278', 'P00742'),
('DB00001', 'SMP0000278', 'P02671'),
('DB00001', 'SMP0000278', 'P02675'),
('DB00001', 'SMP0000278', 'P02679'),
('DB00001', 'SMP0000278', 'P00488'),
('DB00001', 'SMP0000278', 'P05160'),
('DB00001', 'SMP0000278', 'P00747'),
('DB00001', 'SMP0000278', 'P00750'),
('DB00001', 'SMP0000278', 'P08709'),
('DB00001', 'SMP0000278', 'P13726'),
('DB00001', 'SMP0000278', 'Q9BQB6'),
('DB00001', 'SMP0000278', 'P38435'),
('DB00002', 'SMP0000474', 'P00533'),
('DB00006', 'SMP0000277', 'P00734'),
('DB00006', 'SMP0000277', 'P00748'),
('DB00006', 'SMP0000277', 'P02452'),
('DB00006', 'SMP0000277', 'P03952'),
('DB00006', 'SMP0000277', 'P03951'),
('DB00006', 'SMP0000277', 'P00740'),
('DB00006', 'SMP0000277', 'P00451'),
('DB00006', 'SMP0000277', 'P12259'),
('DB00006', 'SMP0000277', 'P00742'),
('DB00006', 'SMP0000277', 'P02671'),
('DB00006', 'SMP0000277', 'P02675'),
('DB00006', 'SMP0000277', 'P02679'),
('DB00006', 'SMP0000277', 'P00488'),
('DB00006', 'SMP0000277', 'P05160'),
('DB00006', 'SMP0000277', 'P00747'),
('DB00006', 'SMP0000277', 'P00750'),
('DB00006', 'SMP0000277', 'P08709'),
('DB00006', 'SMP0000277', 'P13726'),
('DB00006', 'SMP0000277', 'Q9BQB6'),
('DB00006', 'SMP0000277', 'P38435'),
('DB00009', 'SMP0000280', 'P00747'),
('DB00009', 'SMP0000280', 'P00748'),
('DB00009', 'SMP0000280', 'P02452'),
('DB00009', 'SMP0000280', 'P03952'),
('DB00009', 'SMP0000280', 'P03951'),
('DB00009', 'SMP0000280', 'P00740'),
('DB00009', 'SMP0000280', 'P00451'),
('DB00009', 'SMP0000280', 'P00734'),
('DB00009', 'SMP0000280', 'P12259'),
('DB00009', 'SMP0000280', 'P00742'),
('DB00009', 'SMP0000280', 'P02671'),
('DB00009', 'SMP0000280', 'P02675'),
('DB00009', 'SMP0000280', 'P02679'),
('DB00009', 'SMP0000280', 'P00488'),
('DB00009', 'SMP0000280', 'P05160'),
('DB00009', 'SMP0000280', 'P00750'),
('DB00009', 'SMP0000280', 'P08709'),
('DB00009', 'SMP0000280', 'P13726'),
('DB00009', 'SMP0000280', 'Q9BQB6'),
('DB00009', 'SMP0000280', 'P38435');








