import svgwrite
# from svgwrite import cm, mm   

def draw_gene_skil(name, prom_len=0, tfbs_col={}):
	# Set parameter for display gene structure
	max_prom_len = 1500
	px_margin_left = 10
	px_margin_top = 80
	px_start_gene = 800
	
	# Divied drawing object into 4 part: DNA, gene, TLS, and promoter region
	px_per_nt = ( px_start_gene - px_margin_left ) / max_prom_len
	print(px_per_nt, "px per nucleotide")
	px_prom_end = px_margin_left + px_per_nt * prom_len
	print(px_prom_end)
	px_prom_start = px_margin_left + px_start_gene - px_prom_end
	print(px_prom_start)
	# Initial draw window
	dwg = svgwrite.Drawing(name+'.svg', (px_start_gene + 100, 2000), profile='tiny', debug=True)

	# drawing DNA line
	# g_struct = dwg.add(dwg.g(style="font-size:30;font-family:Comic Sans MS, Arial;font-weight:bold;font-style:oblique;stroke:black;stroke-width:1;fill:none"))
	g_struct = dwg.add(dwg.g(id='promoter', stroke='gray'))
	g_struct.add(dwg.line(start=(px_margin_left, px_margin_top) , end=(px_start_gene, px_margin_top)))
	
	# drawing gene box
	g_struct.add(dwg.rect(insert=(px_start_gene, px_margin_top-12), size=(80, 25), fill='#E74C3C', stroke_width=0))

	# drawing TLS
	g_struct.add(dwg.polyline([(px_start_gene, px_margin_top), 
										(px_start_gene, px_margin_top-40), 
										(px_start_gene + 30, px_margin_top-40),
										(px_start_gene + 25, px_margin_top-45),
										(px_start_gene + 30, px_margin_top-40),
										(px_start_gene + 25, px_margin_top-35)
										], fill='none', stroke='gray'))
	g_struct.add(dwg.text('TLS', insert=(px_start_gene, px_margin_top-43), font_size='10px', font_family='Helvetica Neue'))
	g_struct.add(dwg.text(name, insert=(px_start_gene+5, px_margin_top-21), font_size='10px', font_family='Helvetica Neue'))

	# drawing promoter region
	g_struct.add(dwg.rect(insert=(px_prom_start, px_margin_top-12), size=(px_prom_end-px_margin_left, 25), fill='#ECF0F1', stroke_width=0, opacity=0.7))

	i = 0
	for tfbs_id in sorted(tfbs_col.keys()):
		g_struct = dwg.add(dwg.g(id=tfbs_id))
		px_tfbs_top = px_margin_top + 20 + 15*i
		g_struct.add(dwg.text(tfbs_id, insert=(px_start_gene+5, px_tfbs_top + 10 ), font_size='10px', font_family='Helvetica Neue'))
		for pos in tfbs_col[tfbs_id]:
			px_start_tfbs = px_prom_end + (pos * px_per_nt) 
			print("px_prom_end=", px_prom_end, "pos=", pos, "start=", px_start_tfbs)
			g_struct.add(dwg.rect(insert=(px_start_tfbs, px_tfbs_top), size=(10, 10), fill='#E74C3C', stroke_width=0))
		i+=1
	dwg.save()


if __name__ == '__main__':
	# basic_shapes('basic_shapes.svg')

	tfbs_on_prom = '''Symbol	Promoter of gene	TFBS	Position_related_TLS	motif_name
AtSUC1	AT1G71880	TF_motif_seq_0282	-216	POLASIG1
AtSUC1	AT1G71880	TF_motif_seq_0282	-78	POLASIG1
AtSUC1	AT1G71880	TF_motif_seq_0286	-1104	HEXMOTIFTAH3H4
AtSUC1	AT1G71880	TF_motif_seq_0296	-832	S1FBOXSORPS1L21
AtSUC1	AT1G71880	TF_motif_seq_0300	-314	CACGTGMOTIF
AtSUC1	AT1G71880	TF_motif_seq_0302	-1091	EBOXBNNAPA
AtSUC1	AT1G71880	TF_motif_seq_0302	-570	EBOXBNNAPA
AtSUC1	AT1G71880	TF_motif_seq_0302	-399	EBOXBNNAPA
AtSUC1	AT1G71880	TF_motif_seq_0302	-314	EBOXBNNAPA
AtSUC1	AT1G71880	TF_motif_seq_0302	-237	EBOXBNNAPA
AtSUC1	AT1G71880	TF_motif_seq_0313	-1489	MYBCORE
AtSUC1	AT1G71880	TF_motif_seq_0337	-1371	TATABOX5
AtSUC1	AT1G71880	TF_motif_seq_0337	-1319	TATABOX5
AtSUC1	AT1G71880	TF_motif_seq_0337	-612	TATABOX5
AtSUC1	AT1G71880	TF_motif_seq_0337	-608	TATABOX5
AtSUC1	AT1G71880	TF_motif_seq_0347	-1285	POLASIG2
AtSUC1	AT1G71880	TF_motif_seq_0347	-372	POLASIG2
AtSUC1	AT1G71880	TF_motif_seq_0347	-283	POLASIG2
AtSUC1	AT1G71880	TF_motif_seq_0025	-185	TATABOX1
AtSUC1	AT1G71880	TF_motif_seq_0245	-1190	GTGANTG10
AtSUC1	AT1G71880	TF_motif_seq_0245	-1172	GTGANTG10
AtSUC1	AT1G71880	TF_motif_seq_0245	-1067	GTGANTG10
AtSUC1	AT1G71880	TF_motif_seq_0245	-978	GTGANTG10
AtSUC1	AT1G71880	TF_motif_seq_0245	-825	GTGANTG10
AtSUC1	AT1G71880	TF_motif_seq_0245	-819	GTGANTG10
AtSUC1	AT1G71880	TF_motif_seq_0245	-739	GTGANTG10
AtSUC1	AT1G71880	TF_motif_seq_0245	-565	GTGANTG10
AtSUC1	AT1G71880	TF_motif_seq_0245	-556	GTGANTG10
AtSUC1	AT1G71880	TF_motif_seq_0245	-429	GTGANTG10
AtSUC1	AT1G71880	TF_motif_seq_0248	-471	MYBCOREATCYCB1
AtSUC1	AT1G71880	TF_motif_seq_0250	-1454	POLLEN1LELAT52
AtSUC1	AT1G71880	TF_motif_seq_0250	-497	POLLEN1LELAT52
AtSUC1	AT1G71880	TF_motif_seq_0250	-422	POLLEN1LELAT52
AtSUC1	AT1G71880	TF_motif_seq_0250	-388	POLLEN1LELAT52
AtSUC1	AT1G71880	TF_motif_seq_0250	-226	POLLEN1LELAT52
AtSUC1	AT1G71880	TF_motif_seq_0250	-109	POLLEN1LELAT52
AtSUC1	AT1G71880	TF_motif_seq_0250	-89	POLLEN1LELAT52
AtSUC1	AT1G71880	TF_motif_seq_0250	-83	POLLEN1LELAT52
AtSUC1	AT1G71880	TF_motif_seq_0262	-1155	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1096	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1033	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-976	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-848	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-576	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0263	-995	SORLIP1AT
AtSUC1	AT1G71880	TF_motif_seq_0272	-564	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1459	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0277	-600	REALPHALGLHCB21
AtSUC1	AT1G71880	TF_motif_seq_0277	-376	REALPHALGLHCB21
AtSUC1	AT1G71880	TF_motif_seq_0295	-499	BOXIINTPATPB
AtSUC1	AT1G71880	TF_motif_seq_0311	-1035	REBETALGLHCB21
AtSUC1	AT1G71880	TF_motif_seq_0311	-888	REBETALGLHCB21
AtSUC1	AT1G71880	TF_motif_seq_0317	-1033	IBOX
AtSUC1	AT1G71880	TF_motif_seq_0317	-848	IBOX
AtSUC1	AT1G71880	TF_motif_seq_0321	-1217	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0321	-1155	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0321	-976	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0321	-950	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0321	-798	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0321	-576	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0321	-387	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0321	-253	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0321	-225	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0321	-108	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0321	-88	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0321	-82	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0371	-1033	IBOXCORENT
AtSUC1	AT1G71880	TF_motif_seq_0383	-641	TATABOX2
AtSUC1	AT1G71880	TF_motif_seq_0383	-543	TATABOX2
AtSUC1	AT1G71880	TF_motif_seq_0383	-184	TATABOX2
AtSUC1	AT1G71880	TF_motif_seq_0384	-1345	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0440	-600	MYBPLANT
AtSUC1	AT1G71880	TF_motif_seq_0443	-1081	LECPLEACS2
AtSUC1	AT1G71880	TF_motif_seq_0457	-56	PYRIMIDINEBOXHVEPB1
AtSUC1	AT1G71880	TF_motif_seq_0460	-1268	INRNTPSADB
AtSUC1	AT1G71880	TF_motif_seq_0460	-659	INRNTPSADB
AtSUC1	AT1G71880	TF_motif_seq_0460	-207	INRNTPSADB
AtSUC1	AT1G71880	TF_motif_seq_0093	-1429	AT1BOX
AtSUC1	AT1G71880	TF_motif_seq_0093	-1429	AT1BOX
AtSUC1	AT1G71880	TF_motif_seq_0142	-1126	PALBOXPPC
AtSUC1	AT1G71880	TF_motif_seq_0225	-252	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0225	-142	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0225	-129	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0225	-128	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0225	-127	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0225	-124	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0225	-123	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0225	-122	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0225	-107	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0225	-106	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0225	-105	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0225	-99	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0225	-98	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0225	-97	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0225	-96	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0225	-95	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0225	-94	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0225	-93	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0225	-42	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0225	-38	AGTACSAO
AtSUC1	AT1G71880	TF_motif_seq_0258	-1387	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0258	-1385	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0258	-1220	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0258	-1123	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0258	-1118	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0258	-1037	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0258	-991	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0258	-967	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0258	-890	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0258	-829	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0258	-802	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0258	-800	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0258	-709	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0258	-578	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0258	-508	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0258	-458	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0258	-318	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0258	-306	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0258	-255	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0258	-157	LTRECOREATCOR15
AtSUC1	AT1G71880	TF_motif_seq_0271	-1488	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-1458	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-1388	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-1310	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-1269	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-1261	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-1221	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-1127	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-1106	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-1103	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-1071	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-1068	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-921	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-904	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-900	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-856	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-820	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-809	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-564	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-408	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-402	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-395	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-361	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-317	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-153	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0271	-137	ASF1MOTIFCAMV
AtSUC1	AT1G71880	TF_motif_seq_0282	-609	POLASIG1
AtSUC1	AT1G71880	TF_motif_seq_0282	-491	POLASIG1
AtSUC1	AT1G71880	TF_motif_seq_0282	-446	POLASIG1
AtSUC1	AT1G71880	TF_motif_seq_0296	-1054	S1FBOXSORPS1L21
AtSUC1	AT1G71880	TF_motif_seq_0296	-646	S1FBOXSORPS1L21
AtSUC1	AT1G71880	TF_motif_seq_0300	-1070	CACGTGMOTIF
AtSUC1	AT1G71880	TF_motif_seq_0300	-1070	CACGTGMOTIF
AtSUC1	AT1G71880	TF_motif_seq_0300	-399	CACGTGMOTIF
AtSUC1	AT1G71880	TF_motif_seq_0300	-399	CACGTGMOTIF
AtSUC1	AT1G71880	TF_motif_seq_0300	-314	CACGTGMOTIF
AtSUC1	AT1G71880	TF_motif_seq_0300	-237	CACGTGMOTIF
AtSUC1	AT1G71880	TF_motif_seq_0300	-237	CACGTGMOTIF
AtSUC1	AT1G71880	TF_motif_seq_0302	-1091	EBOXBNNAPA
AtSUC1	AT1G71880	TF_motif_seq_0302	-570	EBOXBNNAPA
AtSUC1	AT1G71880	TF_motif_seq_0302	-399	EBOXBNNAPA
AtSUC1	AT1G71880	TF_motif_seq_0302	-314	EBOXBNNAPA
AtSUC1	AT1G71880	TF_motif_seq_0302	-237	EBOXBNNAPA
AtSUC1	AT1G71880	TF_motif_seq_0313	-321	MYBCORE
AtSUC1	AT1G71880	TF_motif_seq_0337	-591	TATABOX5
AtSUC1	AT1G71880	TF_motif_seq_0337	-250	TATABOX5
AtSUC1	AT1G71880	TF_motif_seq_0337	-217	TATABOX5
AtSUC1	AT1G71880	TF_motif_seq_0337	-79	TATABOX5
AtSUC1	AT1G71880	TF_motif_seq_0347	-1474	POLASIG2
AtSUC1	AT1G71880	TF_motif_seq_0347	-1447	POLASIG2
AtSUC1	AT1G71880	TF_motif_seq_0347	-1343	POLASIG2
AtSUC1	AT1G71880	TF_motif_seq_0347	-1150	POLASIG2
AtSUC1	AT1G71880	TF_motif_seq_0347	-1149	POLASIG2
AtSUC1	AT1G71880	TF_motif_seq_0347	-840	POLASIG2
AtSUC1	AT1G71880	TF_motif_seq_0347	-839	POLASIG2
AtSUC1	AT1G71880	TF_motif_seq_0376	-1402	MYBGAHV
AtSUC1	AT1G71880	TF_motif_seq_0376	-1323	MYBGAHV
AtSUC1	AT1G71880	TF_motif_seq_0376	-1251	MYBGAHV
AtSUC1	AT1G71880	TF_motif_seq_0376	-884	MYBGAHV
AtSUC1	AT1G71880	TF_motif_seq_0379	-1402	AMYBOX1
AtSUC1	AT1G71880	TF_motif_seq_0379	-1323	AMYBOX1
AtSUC1	AT1G71880	TF_motif_seq_0379	-1251	AMYBOX1
AtSUC1	AT1G71880	TF_motif_seq_0379	-884	AMYBOX1
AtSUC1	AT1G71880	TF_motif_seq_0381	-1485	NAPINMOTIFBN
AtSUC1	AT1G71880	TF_motif_seq_0381	-535	NAPINMOTIFBN
AtSUC1	AT1G71880	TF_motif_seq_0381	-236	NAPINMOTIFBN
AtSUC1	AT1G71880	TF_motif_seq_0386	-1467	AMYBOX2
AtSUC1	AT1G71880	TF_motif_seq_0386	-1273	AMYBOX2
AtSUC1	AT1G71880	TF_motif_seq_0386	-1099	AMYBOX2
AtSUC1	AT1G71880	TF_motif_seq_0410	-992	ZDNAFORMINGATCAB1
AtSUC1	AT1G71880	TF_motif_seq_0410	-315	ZDNAFORMINGATCAB1
AtSUC1	AT1G71880	TF_motif_seq_0410	-315	ZDNAFORMINGATCAB1
AtSUC1	AT1G71880	TF_motif_seq_0410	-27	ZDNAFORMINGATCAB1
AtSUC1	AT1G71880	TF_motif_seq_0411	-1056	S1FSORPL21
AtSUC1	AT1G71880	TF_motif_seq_0411	-832	S1FSORPL21
AtSUC1	AT1G71880	TF_motif_seq_0411	-648	S1FSORPL21
AtSUC1	AT1G71880	TF_motif_seq_0001	-139	LREBOXIPCCHS1
AtSUC1	AT1G71880	TF_motif_seq_0005	-176	MRNA3ENDTAH3
AtSUC1	AT1G71880	TF_motif_seq_0007	-1046	D1GMAUX28
AtSUC1	AT1G71880	TF_motif_seq_0007	-535	D1GMAUX28
AtSUC1	AT1G71880	TF_motif_seq_0007	-437	D1GMAUX28
AtSUC1	AT1G71880	TF_motif_seq_0015	-987	CIACADIANLELHC
AtSUC1	AT1G71880	TF_motif_seq_0024	-1103	JASE1ATOPR1
AtSUC1	AT1G71880	TF_motif_seq_0029	-316	ACEATCHS
AtSUC1	AT1G71880	TF_motif_seq_0029	-316	ACEATCHS
AtSUC1	AT1G71880	TF_motif_seq_0053	-1169	SORLREP5AT
AtSUC1	AT1G71880	TF_motif_seq_0053	-397	SORLREP5AT
AtSUC1	AT1G71880	TF_motif_seq_0056	-287	ACGTSEED2
AtSUC1	AT1G71880	TF_motif_seq_0065	-1112	SPHZMC1
AtSUC1	AT1G71880	TF_motif_seq_0065	-1077	SPHZMC1
AtSUC1	AT1G71880	TF_motif_seq_0079	-1494	C1MOTIFZMBZ2
AtSUC1	AT1G71880	TF_motif_seq_0148	-839	HBOXCONSENSUSPVCHS
AtSUC1	AT1G71880	TF_motif_seq_0148	-306	HBOXCONSENSUSPVCHS
AtSUC1	AT1G71880	TF_motif_seq_0148	-186	HBOXCONSENSUSPVCHS
AtSUC1	AT1G71880	TF_motif_seq_0194	-379	ANAEROBICCISZMGAPC4
AtSUC1	AT1G71880	TF_motif_seq_0218	-435	SUREAHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0218	-104	SUREAHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0232	-1013	OCETYPEIIINTHISTONE
AtSUC1	AT1G71880	TF_motif_seq_0245	-1309	GTGANTG10
AtSUC1	AT1G71880	TF_motif_seq_0245	-1260	GTGANTG10
AtSUC1	AT1G71880	TF_motif_seq_0245	-1207	GTGANTG10
AtSUC1	AT1G71880	TF_motif_seq_0245	-808	GTGANTG10
AtSUC1	AT1G71880	TF_motif_seq_0245	-619	GTGANTG10
AtSUC1	AT1G71880	TF_motif_seq_0245	-401	GTGANTG10
AtSUC1	AT1G71880	TF_motif_seq_0245	-290	GTGANTG10
AtSUC1	AT1G71880	TF_motif_seq_0245	-152	GTGANTG10
AtSUC1	AT1G71880	TF_motif_seq_0245	-136	GTGANTG10
AtSUC1	AT1G71880	TF_motif_seq_0248	-1489	MYBCOREATCYCB1
AtSUC1	AT1G71880	TF_motif_seq_0248	-1364	MYBCOREATCYCB1
AtSUC1	AT1G71880	TF_motif_seq_0248	-1363	MYBCOREATCYCB1
AtSUC1	AT1G71880	TF_motif_seq_0248	-1040	MYBCOREATCYCB1
AtSUC1	AT1G71880	TF_motif_seq_0248	-901	MYBCOREATCYCB1
AtSUC1	AT1G71880	TF_motif_seq_0248	-708	MYBCOREATCYCB1
AtSUC1	AT1G71880	TF_motif_seq_0248	-578	MYBCOREATCYCB1
AtSUC1	AT1G71880	TF_motif_seq_0248	-529	MYBCOREATCYCB1
AtSUC1	AT1G71880	TF_motif_seq_0248	-508	MYBCOREATCYCB1
AtSUC1	AT1G71880	TF_motif_seq_0248	-458	MYBCOREATCYCB1
AtSUC1	AT1G71880	TF_motif_seq_0248	-433	MYBCOREATCYCB1
AtSUC1	AT1G71880	TF_motif_seq_0248	-410	MYBCOREATCYCB1
AtSUC1	AT1G71880	TF_motif_seq_0248	-362	MYBCOREATCYCB1
AtSUC1	AT1G71880	TF_motif_seq_0248	-355	MYBCOREATCYCB1
AtSUC1	AT1G71880	TF_motif_seq_0248	-340	MYBCOREATCYCB1
AtSUC1	AT1G71880	TF_motif_seq_0248	-320	MYBCOREATCYCB1
AtSUC1	AT1G71880	TF_motif_seq_0248	-171	MYBCOREATCYCB1
AtSUC1	AT1G71880	TF_motif_seq_0248	-119	MYBCOREATCYCB1
AtSUC1	AT1G71880	TF_motif_seq_0250	-681	POLLEN1LELAT52
AtSUC1	AT1G71880	TF_motif_seq_0250	-275	POLLEN1LELAT52
AtSUC1	AT1G71880	TF_motif_seq_0250	-203	POLLEN1LELAT52
AtSUC1	AT1G71880	TF_motif_seq_0250	-67	POLLEN1LELAT52
AtSUC1	AT1G71880	TF_motif_seq_0250	-62	POLLEN1LELAT52
AtSUC1	AT1G71880	TF_motif_seq_0250	-41	POLLEN1LELAT52
AtSUC1	AT1G71880	TF_motif_seq_0259	-1221	CGACGOSAMY3
AtSUC1	AT1G71880	TF_motif_seq_0259	-1221	CGACGOSAMY3
AtSUC1	AT1G71880	TF_motif_seq_0259	-1119	CGACGOSAMY3
AtSUC1	AT1G71880	TF_motif_seq_0259	-1106	CGACGOSAMY3
AtSUC1	AT1G71880	TF_motif_seq_0259	-1103	CGACGOSAMY3
AtSUC1	AT1G71880	TF_motif_seq_0259	-1071	CGACGOSAMY3
AtSUC1	AT1G71880	TF_motif_seq_0259	-918	CGACGOSAMY3
AtSUC1	AT1G71880	TF_motif_seq_0259	-710	CGACGOSAMY3
AtSUC1	AT1G71880	TF_motif_seq_0259	-411	CGACGOSAMY3
AtSUC1	AT1G71880	TF_motif_seq_0259	-408	CGACGOSAMY3
AtSUC1	AT1G71880	TF_motif_seq_0259	-191	CGACGOSAMY3
AtSUC1	AT1G71880	TF_motif_seq_0261	-1453	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-1309	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-1113	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-1044	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-972	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-967	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-930	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-892	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-762	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-687	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-674	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-582	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-565	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-517	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-496	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-427	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-425	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-423	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-401	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-378	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-335	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-316	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-311	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-309	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-264	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-242	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-209	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-168	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-166	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-161	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-114	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-42	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0261	-31	SURECOREATSULTR11
AtSUC1	AT1G71880	TF_motif_seq_0262	-1496	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1464	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1403	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1383	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1373	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1371	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1368	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1360	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1343	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1319	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1311	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1275	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1274	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1253	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1252	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1230	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1225	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1217	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1185	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1171	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1170	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-1061	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-974	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-945	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-943	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-936	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-935	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-930	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-911	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-886	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-880	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-872	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-859	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-834	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-824	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-814	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-798	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-764	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-714	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-704	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-674	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-664	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-641	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-624	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-612	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-608	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-590	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-582	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-574	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-560	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-554	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-543	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-519	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-490	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-483	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-460	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-445	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-423	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-387	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-331	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-259	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-253	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-249	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-247	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-244	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-230	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-225	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-216	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-184	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-168	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-163	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-108	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-88	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-82	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-78	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-68	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-63	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-54	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0262	-33	IBOXCORE
AtSUC1	AT1G71880	TF_motif_seq_0263	-1389	SORLIP1AT
AtSUC1	AT1G71880	TF_motif_seq_0263	-1309	SORLIP1AT
AtSUC1	AT1G71880	TF_motif_seq_0263	-1241	SORLIP1AT
AtSUC1	AT1G71880	TF_motif_seq_0263	-998	SORLIP1AT
AtSUC1	AT1G71880	TF_motif_seq_0263	-922	SORLIP1AT
AtSUC1	AT1G71880	TF_motif_seq_0263	-843	SORLIP1AT
AtSUC1	AT1G71880	TF_motif_seq_0263	-779	SORLIP1AT
AtSUC1	AT1G71880	TF_motif_seq_0263	-565	SORLIP1AT
AtSUC1	AT1G71880	TF_motif_seq_0263	-401	SORLIP1AT
AtSUC1	AT1G71880	TF_motif_seq_0263	-316	SORLIP1AT
AtSUC1	AT1G71880	TF_motif_seq_0263	-311	SORLIP1AT
AtSUC1	AT1G71880	TF_motif_seq_0263	-298	SORLIP1AT
AtSUC1	AT1G71880	TF_motif_seq_0265	-1120	SORLIP2AT
AtSUC1	AT1G71880	TF_motif_seq_0265	-1044	SORLIP2AT
AtSUC1	AT1G71880	TF_motif_seq_0265	-997	SORLIP2AT
AtSUC1	AT1G71880	TF_motif_seq_0265	-996	SORLIP2AT
AtSUC1	AT1G71880	TF_motif_seq_0265	-892	SORLIP2AT
AtSUC1	AT1G71880	TF_motif_seq_0265	-777	SORLIP2AT
AtSUC1	AT1G71880	TF_motif_seq_0265	-309	SORLIP2AT
AtSUC1	AT1G71880	TF_motif_seq_0272	-1494	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-1458	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-1410	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-1374	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-1337	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-1310	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-1265	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-1259	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-1254	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-1208	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-1191	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-1189	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-1112	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-1103	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-1043	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-966	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-960	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-904	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-877	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-844	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-818	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-812	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-807	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-740	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-738	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-710	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-692	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-686	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-620	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-573	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-518	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-503	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-463	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-416	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-414	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-402	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-400	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-332	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-321	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-317	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-291	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-271	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-265	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-246	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-222	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-135	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-113	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-32	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0272	-11	WBOXHVISO1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1438	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1409	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1403	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1383	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1338	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1311	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1309	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1277	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1264	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1253	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1252	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1243	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1241	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1220	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1169	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1137	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1118	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1107	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1102	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1072	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-1067	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-998	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-922	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-912	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-905	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-873	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-843	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-819	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-808	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-778	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-691	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-626	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-624	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-619	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-565	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-519	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-517	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-484	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-417	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-413	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-407	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-401	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-396	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-360	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-331	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-318	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-300	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-221	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-33	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-31	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0275	-12	WBOXATNPR1
AtSUC1	AT1G71880	TF_motif_seq_0277	-1088	REALPHALGLHCB21
AtSUC1	AT1G71880	TF_motif_seq_0280	-1435	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-1435	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-1304	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-1304	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-1247	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-1247	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-1141	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-1141	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-1093	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-1093	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-494	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-494	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-471	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-471	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-453	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-453	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-410	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-410	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-328	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-328	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-45	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0280	-45	ACGTTBOX
AtSUC1	AT1G71880	TF_motif_seq_0295	-1330	BOXIINTPATPB
AtSUC1	AT1G71880	TF_motif_seq_0295	-40	BOXIINTPATPB
AtSUC1	AT1G71880	TF_motif_seq_0311	-258	REBETALGLHCB21
AtSUC1	AT1G71880	TF_motif_seq_0317	-260	IBOX
AtSUC1	AT1G71880	TF_motif_seq_0321	-1369	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0321	-1368	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0321	-1186	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0321	-705	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0321	-704	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0321	-484	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0321	-69	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0321	-55	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0321	-54	GT1CONSENSUS
AtSUC1	AT1G71880	TF_motif_seq_0328	-1466	TATCCAOSAMY
AtSUC1	AT1G71880	TF_motif_seq_0330	-929	-10PEHVPSBD
AtSUC1	AT1G71880	TF_motif_seq_0330	-793	-10PEHVPSBD
AtSUC1	AT1G71880	TF_motif_seq_0332	-1104	TGACGTVMAMY
AtSUC1	AT1G71880	TF_motif_seq_0352	-316	BOXIIPCCHS
AtSUC1	AT1G71880	TF_motif_seq_0352	-313	BOXIIPCCHS
AtSUC1	AT1G71880	TF_motif_seq_0357	-1002	2SSEEDPROTBANAPA
AtSUC1	AT1G71880	TF_motif_seq_0357	-597	2SSEEDPROTBANAPA
AtSUC1	AT1G71880	TF_motif_seq_0357	-478	2SSEEDPROTBANAPA
AtSUC1	AT1G71880	TF_motif_seq_0358	-411	BP5OSWX
AtSUC1	AT1G71880	TF_motif_seq_0364	-455	AMMORESIVDCRNIA1
AtSUC1	AT1G71880	TF_motif_seq_0365	-1002	CANBNNAPA
AtSUC1	AT1G71880	TF_motif_seq_0370	-225	EECCRCAH1
AtSUC1	AT1G71880	TF_motif_seq_0371	-1155	IBOXCORENT
AtSUC1	AT1G71880	TF_motif_seq_0371	-1096	IBOXCORENT
AtSUC1	AT1G71880	TF_motif_seq_0371	-848	IBOXCORENT
AtSUC1	AT1G71880	TF_motif_seq_0371	-261	IBOXCORENT
AtSUC1	AT1G71880	TF_motif_seq_0372	-1071	ACGTOSGLUB1
AtSUC1	AT1G71880	TF_motif_seq_0372	-829	ACGTOSGLUB1
AtSUC1	AT1G71880	TF_motif_seq_0375	-1162	SEF4MOTIFGM7S
AtSUC1	AT1G71880	TF_motif_seq_0375	-359	SEF4MOTIFGM7S
AtSUC1	AT1G71880	TF_motif_seq_0375	-143	SEF4MOTIFGM7S
AtSUC1	AT1G71880	TF_motif_seq_0382	-1232	SP8BFIBSP8BIB
AtSUC1	AT1G71880	TF_motif_seq_0382	-552	SP8BFIBSP8BIB
AtSUC1	AT1G71880	TF_motif_seq_0383	-1362	TATABOX2
AtSUC1	AT1G71880	TF_motif_seq_0383	-1343	TATABOX2
AtSUC1	AT1G71880	TF_motif_seq_0383	-814	TATABOX2
AtSUC1	AT1G71880	TF_motif_seq_0383	-714	TATABOX2
AtSUC1	AT1G71880	TF_motif_seq_0384	-1430	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-1428	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-1427	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-1426	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-1425	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-1360	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-1359	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-1358	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-1357	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-1356	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-1355	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-1354	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-1353	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-1352	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-1351	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-1350	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-1349	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-1348	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-1347	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-1346	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0384	-555	TATABOX4
AtSUC1	AT1G71880	TF_motif_seq_0387	-1467	TATCCAYMOTIFOSRAMY3D
AtSUC1	AT1G71880	TF_motif_seq_0387	-1273	TATCCAYMOTIFOSRAMY3D
AtSUC1	AT1G71880	TF_motif_seq_0387	-1099	TATCCAYMOTIFOSRAMY3D
AtSUC1	AT1G71880	TF_motif_seq_0393	-1266	CMSRE1IBSPOA
AtSUC1	AT1G71880	TF_motif_seq_0393	-1107	CMSRE1IBSPOA
AtSUC1	AT1G71880	TF_motif_seq_0393	-1072	CMSRE1IBSPOA
AtSUC1	AT1G71880	TF_motif_seq_0393	-409	CMSRE1IBSPOA
AtSUC1	AT1G71880	TF_motif_seq_0399	-1460	WBBOXPCWRKY1
AtSUC1	AT1G71880	TF_motif_seq_0399	-874	WBBOXPCWRKY1
AtSUC1	AT1G71880	TF_motif_seq_0399	-692	WBBOXPCWRKY1
AtSUC1	AT1G71880	TF_motif_seq_0399	-222	WBBOXPCWRKY1
AtSUC1	AT1G71880	TF_motif_seq_0400	-1210	MRNASTA2CRPSBD
AtSUC1	AT1G71880	TF_motif_seq_0400	-738	MRNASTA2CRPSBD
AtSUC1	AT1G71880	TF_motif_seq_0405	-317	LRENPCABE
AtSUC1	AT1G71880	TF_motif_seq_0407	-1485	SP8BFIBSP8AIB
AtSUC1	AT1G71880	TF_motif_seq_0407	-1376	SP8BFIBSP8AIB
AtSUC1	AT1G71880	TF_motif_seq_0407	-1141	SP8BFIBSP8AIB
AtSUC1	AT1G71880	TF_motif_seq_0407	-1027	SP8BFIBSP8AIB
AtSUC1	AT1G71880	TF_motif_seq_0407	-964	SP8BFIBSP8AIB
AtSUC1	AT1G71880	TF_motif_seq_0407	-808	SP8BFIBSP8AIB
AtSUC1	AT1G71880	TF_motif_seq_0407	-788	SP8BFIBSP8AIB
AtSUC1	AT1G71880	TF_motif_seq_0407	-619	SP8BFIBSP8AIB
AtSUC1	AT1G71880	TF_motif_seq_0407	-535	SP8BFIBSP8AIB
AtSUC1	AT1G71880	TF_motif_seq_0407	-533	SP8BFIBSP8AIB
AtSUC1	AT1G71880	TF_motif_seq_0407	-530	SP8BFIBSP8AIB
AtSUC1	AT1G71880	TF_motif_seq_0407	-488	SP8BFIBSP8AIB
AtSUC1	AT1G71880	TF_motif_seq_0407	-465	SP8BFIBSP8AIB
AtSUC1	AT1G71880	TF_motif_seq_0407	-432	SP8BFIBSP8AIB
AtSUC1	AT1G71880	TF_motif_seq_0407	-288	SP8BFIBSP8AIB
AtSUC1	AT1G71880	TF_motif_seq_0407	-269	SP8BFIBSP8AIB
AtSUC1	AT1G71880	TF_motif_seq_0408	-990	AGMOTIFNTMYB2
AtSUC1	AT1G71880	TF_motif_seq_0408	-874	AGMOTIFNTMYB2
AtSUC1	AT1G71880	TF_motif_seq_0413	-1479	PE2FNTRNR1A
AtSUC1	AT1G71880	TF_motif_seq_0413	-896	PE2FNTRNR1A
AtSUC1	AT1G71880	TF_motif_seq_0413	-821	PE2FNTRNR1A
AtSUC1	AT1G71880	TF_motif_seq_0413	-366	PE2FNTRNR1A
AtSUC1	AT1G71880	TF_motif_seq_0413	-169	PE2FNTRNR1A
AtSUC1	AT1G71880	TF_motif_seq_0413	-27	PE2FNTRNR1A
AtSUC1	AT1G71880	TF_motif_seq_0415	-474	CDA1ATCAB2
AtSUC1	AT1G71880	TF_motif_seq_0435	-1172	PIATGAPB
AtSUC1	AT1G71880	TF_motif_seq_0435	-978	PIATGAPB
AtSUC1	AT1G71880	TF_motif_seq_0435	-825	PIATGAPB
AtSUC1	AT1G71880	TF_motif_seq_0440	-830	MYBPLANT
AtSUC1	AT1G71880	TF_motif_seq_0443	-1290	LECPLEACS2
AtSUC1	AT1G71880	TF_motif_seq_0443	-608	LECPLEACS2
AtSUC1	AT1G71880	TF_motif_seq_0443	-280	LECPLEACS2
AtSUC1	AT1G71880	TF_motif_seq_0455	-1367	E2FANTRNR
AtSUC1	AT1G71880	TF_motif_seq_0455	-703	E2FANTRNR
AtSUC1	AT1G71880	TF_motif_seq_0457	-1218	PYRIMIDINEBOXHVEPB1
AtSUC1	AT1G71880	TF_motif_seq_0457	-1217	PYRIMIDINEBOXHVEPB1
AtSUC1	AT1G71880	TF_motif_seq_0457	-388	PYRIMIDINEBOXHVEPB1
AtSUC1	AT1G71880	TF_motif_seq_0457	-109	PYRIMIDINEBOXHVEPB1
AtSUC1	AT1G71880	TF_motif_seq_0457	-108	PYRIMIDINEBOXHVEPB1
AtSUC1	AT1G71880	TF_motif_seq_0457	-57	PYRIMIDINEBOXHVEPB1
AtSUC1	AT1G71880	TF_motif_seq_0457	-15	PYRIMIDINEBOXHVEPB1
AtSUC1	AT1G71880	TF_motif_seq_0460	-420	INRNTPSADB
AtSUC1	AT1G71880	TF_motif_seq_0469	-543	SEF1MOTIF'''
	tfbs_on_prom = tfbs_on_prom.split('\n')[1:]
	for i in range(len(tfbs_on_prom)):
		tfbs_on_prom[i] = tfbs_on_prom[i].split('\t')
	tfbs_col = {}
	for tfbs in tfbs_on_prom:
		if tfbs[4] not in tfbs_col.keys():
			tfbs_col[tfbs[4]] = [int(tfbs[3])]
		else:
			tfbs_col[tfbs[4]].append(int(tfbs[3]))
	# print(tfbs_col)

	draw_gene_skil('AT1G71880', 1500, tfbs_col)
	# draw_tfbs(tfbs_col)