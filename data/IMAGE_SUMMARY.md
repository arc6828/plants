# 📊 รายงานสรุปจำนวนรูปภาพพรรณไม้ (Image Database Summary)

เอกสารฉบับนี้แสดงการวิเคราะห์เปรียบเทียบระหว่าง ข้อมูลดิบที่สืบค้นมาได้จาก GBIF API และ ข้อมูลหลังผ่านการคัดกรองเพื่อใช้ฝึกสอนตัวแบบจำลอง (Deep Learning Dataset)

---

## 🎯 1. ข้อมูลรูปภาพหลังการคัดกรองแล้ว (Filtered & Capped Dataset - ที่ใช้จริงในการเทรน)

เป็นข้อมูลที่คัดเอาเฉพาะพืชที่มีรูปภาพ**ไม่ต่ำกว่า 100 รูป** และคัดเลือกภาพของชนิดพืชที่เกิน**ให้เหลือ 100 รูปพอดีเป๊ะ** เพื่อสร้างความสมดุลของการฝึกเรียนรู้ (Balanced Train Dataset):

* **จำนวนพรรณไม้ที่ผ่านเกณฑ์นำไปเทรน:** **166 ชนิด (Classes)**
* **จำนวนรูปภาพเป้าหมายคัดกรอง:** **16,600 ภาพ** (100 รูป/ชนิด)
* **จำนวนรูปภาพที่โหลดสำเร็จ (ก่อน Resize):** **15,902 ภาพ**
* **จำนวนรูปภาพหลัง Resize ได้จริง:** **15,891 ภาพ**
* **ตำแหน่งไฟล์คลังข้อมูลใช้จริง:** [VRU_image_links_filtered.json](VRU_image_links_filtered.json)
* **การปรับขนาดรูปภาพ (Resize):** ปรับขนาดด้วยวิธีเติมขอบว่าง (384x384 พิกเซล) ช่วยลดขนาดไฟล์ของโฟลเดอร์รูปภาพจาก **36.3 GB** เหลือเพียง **545.7 MB** (ประหยัดพื้นที่จัดเก็บได้ถึง 98.5%)


| ลำดับที่ | ชื่อพืชภาษาไทย | ชื่อวิทยาศาสตร์ | ดาวน์โหลดสำเร็จ (ภาพ) | Resize สำเร็จ (ภาพ) |
| :---: | :--- | :--- | :---: | :---: |
| 1 | กรรณิกา | *Nyctanthes arbor-tristis L.* | 100 | 100 |
| 2 | กระดังงาจีน | *Artabotrys hexapetalus (L. f.) Bhandari* | 93 | 93 |
| 3 | กระถิน | *Leucaena leucocephala (Lam.) de Wit* | 100 | 100 |
| 4 | กระถินณรงค์ | *Acacia auriculiformis A. Cunn. ex Benth.* | 100 | 100 |
| 5 | กระทิง | *Calophyllum inophyllum L.* | 100 | 100 |
| 6 | กระทุ่มนา | *Mitragyna diversifolia (Wall. ex G. Don) Havil.* | 81 | 81 |
| 7 | กระท้อน | *Sandoricum koetjape (Burm. f.) Merr.* | 97 | 97 |
| 8 | กระพี้จั่น | *Millettia brandisiana Kurz* | 79 | 79 |
| 9 | กร่าง | *Ficus altissima Blume* | 100 | 100 |
| 10 | กล้วยพัด | *Ravenala madagascariensis Sonn.* | 100 | 100 |
| 11 | กะตังใบ | *Leea indica (Burm. f.) Merr.* | 100 | 100 |
| 12 | กันเกรา | *Fagraea fragrans Roxb.* | 100 | 100 |
| 13 | การะเกด | *Pandanus tectorius Parkinson ex Du Roi* | 100 | 100 |
| 14 | การะเกดหนู | *Pandanus pygmaeus Thouars* | 90 | 90 |
| 15 | กุหลาบมอญ | *Rosa ×damascena Herrm.* | 82 | 81 |
| 16 | ขนุน | *Artocarpus heterophyllus Lam.* | 100 | 100 |
| 17 | ขี้เหล็ก | *Senna siamea (Lam.) H. S. Irwin & Barneby* | 100 | 100 |
| 18 | ข่อย | *Streblus asper Lour.* | 100 | 100 |
| 19 | คนทีสอ | *Vitex trifolia L. subsp. trifolia* | 99 | 99 |
| 20 | คนทีเขมา | *Vitex negundo L.* | 100 | 100 |
| 21 | คริสติน่า | *Syzygium australe (J.C.Wendl. ex Link) B.Hyland* | 99 | 99 |
| 22 | คัดเค้า | *Oxyceros horridus Lour.* | 59 | 59 |
| 23 | จันทน์ผา | *Dracaena cochinchinensis (Lour.) S. C. Chen* | 100 | 100 |
| 24 | จั๋งญี่ปุ่น | *Rhapis excelsa (Thunb.) Henry* | 100 | 100 |
| 25 | จามจุรี | *Albizia saman (Jacq.) Merr.* | 100 | 100 |
| 26 | จำปี | *Magnolia ×alba (DC.) Figlar* | 96 | 96 |
| 27 | จิกนมยาน | *Barringtonia macrocarpa Hassk.* | 88 | 88 |
| 28 | จิกสวน | *Barringtonia racemosa (L.) Spreng.* | 100 | 100 |
| 29 | ชงโค | *Bauhinia purpurea L.* | 100 | 100 |
| 30 | ชบา | *Hibiscus rosa-sinensis L.* | 100 | 100 |
| 31 | ชมพูพันธุ์ทิพย์ | *Tabebuia rosea (Bertol.) Bertero ex A. DC.* | 100 | 100 |
| 32 | ชมพู่ม่าเหมี่ยว | *Syzygium malaccense (L.) Merr. & L. M. Perry* | 100 | 100 |
| 33 | ชะมวง | *Garcinia cowa Roxb. ex Choisy* | 71 | 71 |
| 34 | ชาฮกเกี้ยน | *Ehretia microphylla Lam.* | 100 | 100 |
| 35 | ชำมะเลียง | *Lepisanthes fruticosa (Roxb.) Leenh.* | 94 | 94 |
| 36 | ช้องนาง | *Thunbergia erecta (Benth.) T. Anderson* | 100 | 100 |
| 37 | ตะขบฝรั่ง | *Muntingia calabura L.* | 100 | 100 |
| 38 | ตะลิงปลิง | *Averrhoa bilimbi L.* | 100 | 100 |
| 39 | ตะเคียนทอง | *Hopea odorata Roxb.* | 90 | 90 |
| 40 | ตะโกนา | *Diospyros rhodocalyx Kurz* | 45 | 45 |
| 41 | ตาล | *Borassus flabellifer L.* | 100 | 100 |
| 42 | ตาลฟ้า | *Bismarckia nobilis Hildebr. & H. Wendl.* | 100 | 100 |
| 43 | ตีนเป็ดน้ำ | *Cerbera odollam Gaertn.* | 100 | 100 |
| 44 | ต้อยติ่ง | *Ruellia tuberosa L.* | 100 | 100 |
| 45 | ทองกวาว | *Butea monosperma (Lam.) Taub.* | 100 | 100 |
| 46 | ทองหลางลาย | *Erythrina variegata L.* | 100 | 100 |
| 47 | ทองอุไร | *Tecoma stans (L.) Juss. ex Kunth* | 100 | 100 |
| 48 | ทับทิม | *Punica granatum L. var. granatum* | 100 | 100 |
| 49 | ธรรมรักษา | *Heliconia psittacorum L. f.* | 100 | 100 |
| 50 | นนทรี | *Peltophorum pterocarpum (DC.) Backer ex K. Heyne* | 100 | 100 |
| 51 | นีออน | *Leucophyllum frutescens (Berland.) I. M. Johnst.* | 100 | 100 |
| 52 | น้อยหน่า | *Annona squamosa L.* | 100 | 100 |
| 53 | บานบุรี | *Cascabela thevetia (L.) Lippold* | 100 | 100 |
| 54 | บาหยา | *Asystasia gangetica (L.) T. Anderson subsp. gangetica* | 100 | 100 |
| 55 | บุนนาค | *Mesua ferrea L.* | 93 | 93 |
| 56 | บุหงาส่าหรี | *Citharexylum spinosum L.* | 100 | 100 |
| 57 | ปรงญี่ปุ่น | *Cycas revoluta Thunb.* | 100 | 100 |
| 58 | ประดู่บ้าน | *Pterocarpus indicus Willd.* | 100 | 100 |
| 59 | ประยงค์ | *Aglaia odorata Lour.* | 98 | 98 |
| 60 | ประเดหวี | *Dracaena fragrans (L.) Ker Gawl.* | 100 | 100 |
| 61 | ปาล์มจีบ | *Licuala grandis H. Wendl.* | 100 | 100 |
| 62 | ปาล์มชวา | *Saribus rotundifolius (Lam.) Blume* | 100 | 100 |
| 63 | ปาล์มน้ำมัน | *Elaeis guineensis Jacq.* | 100 | 100 |
| 64 | ปาล์มพัด | *Pritchardia pacifica Seem. & H. Wendl.* | 100 | 100 |
| 65 | ปาล์มสามทาง | *Dypsis lutescens (H. Wendl.) Beentje & J. Dransf.* | 100 | 100 |
| 66 | ปาล์มสิบสองปันนา | *phoenix roebelenii O'Brien* | 100 | 100 |
| 67 | ปาล์มหางกระรอก | *Wodyetia bifurcata A. K. Irvine* | 100 | 100 |
| 68 | ปีบ | *Millingtonia hortensis L. f.* | 100 | 100 |
| 69 | ปีปทอง | *Radermachera hainanensis Merr.* | 76 | 76 |
| 70 | ผักหวานบ้าน | *Breynia androgyna (L.) Chakrab. & N.P. Balakr.* | 98 | 98 |
| 71 | ฝรั่ง | *Psidium guajava L.* | 100 | 100 |
| 72 | ฝ้าย | *Gossypium herbaceum L.* | 100 | 100 |
| 73 | พยับหมอก | *Plumbago auriculata Lam.* | 100 | 100 |
| 74 | พลับพลึงตีนเป็ด | *Hymenocallis littoralis (Jacq.) Salisb.* | 100 | 100 |
| 75 | พวงทองต้น | *Galphimia gracilis Bartl.* | 100 | 100 |
| 76 | พะยูง | *Dalbergia cochinchinensis Pierre* | 73 | 73 |
| 77 | พิกุล | *Mimusops elengi L.* | 100 | 100 |
| 78 | พุดจีบ | *Tabernaemontana divaricata (L.) R. Br.ex Roem. & Schult.* | 100 | 100 |
| 79 | พุดซ้อน | *Gardenia jasminoides J. Ellis* | 100 | 100 |
| 80 | พุดพิชญา | *Wrightia antidysenterica (L.) R. Br.* | 100 | 100 |
| 81 | พุดศุภโชค (พุดซ้อน) | *Gardenia jasminoides J. Ellis* | 100 | 100 |
| 82 | พุดสามสี | *Brunfelsia uniflora (Pohl) D. Don* | 100 | 100 |
| 83 | พุทธชาดก้านแดง | *Jasminum grandiflorum L.* | 88 | 88 |
| 84 | พุทธรักษา | *Canna indica L.* | 100 | 100 |
| 85 | มะกรูด | *Citrus hystrix DC.* | 100 | 100 |
| 86 | มะกอกน้ำ | *Elaeocarpus hygrophilus Kurz* | 47 | 47 |
| 87 | มะขวิด | *Limonia acidissima L.* | 99 | 99 |
| 88 | มะขาม | *Tamarindus indica L.* | 100 | 100 |
| 89 | มะขามเทศ | *Pithecellobium dulce (Roxb.) Benth.* | 100 | 100 |
| 90 | มะตาด | *Dillenia indica L.* | 100 | 100 |
| 91 | มะตูม | *Aegle marmelos (L.) Corrêa ex Roxb.* | 100 | 100 |
| 92 | มะพร้าว | *Cocos nucifera L.* | 100 | 100 |
| 93 | มะม่วง | *Mangifera indica L.* | 100 | 100 |
| 94 | มะม่วงหิมพานต์ | *Anacardium occidentale L.* | 100 | 100 |
| 95 | มะยงชิด | *Bouea oppositifolia (Roxb.) Meisn.* | 95 | 95 |
| 96 | มะยม | *Phyllanthus acidus (L.) Skeels* | 100 | 100 |
| 97 | มะรุม | *Moringa oleifera Lam.* | 100 | 100 |
| 98 | มะละกอ | *Carica papaya L.* | 100 | 100 |
| 99 | มะลิลา | *Jasminum sambac (L.) Aiton* | 100 | 100 |
| 100 | มะสัง | *Feroniella lucida (Scheff.) Swingle* | 52 | 52 |
| 101 | มะฮอกกานีใบใหญ่ | *Swietenia macrophylla King* | 100 | 100 |
| 102 | มะเฟือง | *Averrhoa carambola L.* | 100 | 100 |
| 103 | มันปู | *Glochidion littorale Blume* | 96 | 96 |
| 104 | มิกกี้เมาส์ | *Ochna thomasiana Engl. & Gilg* | 100 | 100 |
| 105 | ยอ | *Morinda citrifolia L.* | 100 | 100 |
| 106 | ยางนา | *Dipterocarpus alatus Roxb. ex G. Don* | 4 | 4 |
| 107 | ยางอินเดีย | *Ficus elastica Roxb. ex Hornem* | 100 | 100 |
| 108 | ยี่โถ | *Nerium oleander L.* | 100 | 100 |
| 109 | รัก | *Calotropis gigantea (L.) W. T. Aiton* | 100 | 100 |
| 110 | ราชพฤกษ์ | *Cassia fistula L.* | 100 | 100 |
| 111 | ราชาวดี | *Buddleja paniculata Wall.* | 65 | 65 |
| 112 | รำเพย | *Cascabela thevetia (L.) Lippold* | 100 | 100 |
| 113 | ละมุด | *Manilkara zapota (L.) P. Royen* | 100 | 100 |
| 114 | ละมุดเขมร | *Pouteria campechiana (Kunth) Baehni* | 100 | 100 |
| 115 | ลั่นทมแดง | *Plumeria rubra L.* | 100 | 100 |
| 116 | ลิ้นกระบือ | *Excoecaria cochinchinensis Lour. var. cochinchinensis* | 100 | 100 |
| 117 | ว่านธรณีสาร | *Phyllanthus pulcher Wall. ex Müll. Arg.* | 99 | 99 |
| 118 | ว่านเพชรหึง | *Grammatophyllum speciosum Blume* | 100 | 100 |
| 119 | ศรีตรัง | *Jacaranda obtusifolia Bonpl.* | 84 | 84 |
| 120 | สนประดิพัทธ์ | *Casuarina junghuhniana Miq.* | 90 | 90 |
| 121 | สบู่ดำ | *Jatropha curcas L.* | 100 | 100 |
| 122 | สะเดา | *Azadirachta indica A. Juss.* | 100 | 100 |
| 123 | สัก | *Tectona grandis L. f.* | 100 | 100 |
| 124 | สัตบรรณ | *Alstonia scholaris (L.) R. Br.* | 100 | 100 |
| 125 | สารภี | *Mammea siamensis (Miq.) T. Anderson* | 69 | 69 |
| 126 | สาละลังกา | *Couroupita guianensis Aubl.* | 100 | 100 |
| 127 | ส้มจี๊ด | *Citrus japonica Thunb.* | 97 | 97 |
| 128 | ส้มโอ | *Citrus maxima (Burm.) Merr.* | 98 | 98 |
| 129 | หนวดปลาหมึกแคระ | *Schefflera arboricola (Hayata) Hayata cv. Compacta* | 79 | 79 |
| 130 | หนามแดง | *Carissa carandas L.* | 96 | 96 |
| 131 | หมากนวล | *Adonidia merrillii (Becc.) Becc.* | 100 | 100 |
| 132 | หมากเหลือง | *Dypsis lutescens (H. Wendl.) Beentje & J. Dransf.* | 100 | 100 |
| 133 | หม่อน | *Morus alba L.* | 100 | 100 |
| 134 | หว้า | *Syzygium cumini (L.) Skeels* | 100 | 100 |
| 135 | หางนกยูงฝรั่ง | *Delonix regia (Bojer ex Hook.) Raf.* | 100 | 100 |
| 136 | หูกระจง | *Terminalia ivorensis A. Chev.* | 71 | 67 |
| 137 | หูกวาง | *Terminalia catappa L.* | 100 | 100 |
| 138 | หูปลาช่อน | *Acalypha hispida Burm. f.* | 100 | 100 |
| 139 | อินทนิล | *Lagerstroemia speciosa (L.) Pers.* | 100 | 100 |
| 140 | อินทผลัม | *Phoenix dactylifera L.* | 100 | 100 |
| 141 | อโศกเซนคาเบรียล | *Monoon longifolium (Sonn.) B. Xue & R. M. K. Saunders* | 100 | 100 |
| 142 | เชอร์รี่ไทย | *Malpighia glabra L.* | 100 | 100 |
| 143 | เต่าร้าง | *Caryota mitis Lour.* | 100 | 100 |
| 144 | เทียนหยด | *Duranta erecta L.* | 100 | 100 |
| 145 | เพกา | *Oroxylum indicum (L.) Benth. ex Kurz* | 100 | 100 |
| 146 | เล็บมือนาง | *Combretum indicum (L.) De Filipps* | 100 | 100 |
| 147 | เสลา | *Lagerstroemia loudonii Teijsm. & Binn.* | 89 | 83 |
| 148 | เหรียง | *Parkia timoriana (DC.) Merr.* | 97 | 97 |
| 149 | เหลืองปรีดียาธร | *Roseodendron donnell-smithii (Rose) Miranda* | 100 | 100 |
| 150 | เฮลิโคเนีย | *Heliconia rostrata Ruiz. & Pav.* | 100 | 100 |
| 151 | แก้ว | *Murraya paniculata (L.) Jack* | 100 | 100 |
| 152 | แก้วเจ้าจอม | *Guaiacum officinale L.* | 100 | 100 |
| 153 | แคบ้าน | *Sesbania grandiflora (L.) Poir.* | 100 | 100 |
| 154 | แคฝรั่ง | *Gliricidia sepium (Jacq.) Walp.* | 100 | 100 |
| 155 | แคแสด | *Spathodea campanulata P. Beauv.* | 100 | 100 |
| 156 | แปรงล้างขวด | *Callistemon lanceolatus (Sm.) Sweet* | 100 | 100 |
| 157 | แสงจันทร์ | *Pisonia grandis R. Br.* | 89 | 89 |
| 158 | โกงกางเขา | *Fagraea ceilanica Thunb.* | 98 | 98 |
| 159 | โกสน | *Codiaeum variegatum (L.) Rumph. ex A. Juss.* | 100 | 100 |
| 160 | โพขี้นก | *Ficus rumphii Blume* | 100 | 100 |
| 161 | โพศรีมหาโพธิ | *Ficus religiosa L.* | 100 | 100 |
| 162 | โมกบ้าน | *Wrightia religiosa (Teijsm. & Binn.) Benth. ex Kurz* | 100 | 100 |
| 163 | ใบเงิน ใบทอง | *Graptophyllum pictum (L.) Griff.* | 100 | 100 |
| 164 | ไทรทอง | *Ficus microcarpa L. f.* | 100 | 100 |
| 165 | ไทรย้อยใบแหลม | *Ficus benjamina L.* | 100 | 100 |
| 166 | ไผ่ฟิลิปปินส์ | *Dracaena surculosa Lindl.* | 99 | 99 |

---

## 📂 2. ข้อมูลรูปภาพที่ได้จากการค้นหาดิบ (Raw GBIF API Search Results)

เป็นรายการลิงก์ข้อมูลภาพทั้งหมดที่สแกนหาได้ครั้งแรกจาก GBIF API (รวมทั้งสิ้น **25,284 ภาพ** จากพรรณไม้ **176 ชนิด**):

* **ตำแหน่งไฟล์ดิบ:** [VRU_image_links.json](VRU_image_links.json)

| ลำดับที่ | ชื่อพืชภาษาไทย | ชื่อวิทยาศาสตร์ | จำนวนรูปภาพดิบที่พบ |
| :---: | :--- | :--- | :---: |
| 1 | ปาล์มสิบสองปันนา | *phoenix roebelenii O'Brien* | 300 |
| 2 | กรรณิกา | *Nyctanthes arbor-tristis L.* | 150 |
| 3 | กะตังใบ | *Leea indica (Burm. f.) Merr.* | 150 |
| 4 | กระถิน | *Leucaena leucocephala (Lam.) de Wit* | 150 |
| 5 | กระถินณรงค์ | *Acacia auriculiformis A. Cunn. ex Benth.* | 150 |
| 6 | กระดังงาจีน | *Artabotrys hexapetalus (L. f.) Bhandari* | 150 |
| 7 | กระท้อน | *Sandoricum koetjape (Burm. f.) Merr.* | 150 |
| 8 | กระทิง | *Calophyllum inophyllum L.* | 150 |
| 9 | กระทุ่มนา | *Mitragyna diversifolia (Wall. ex G. Don) Havil.* | 150 |
| 10 | กระพี้จั่น | *Millettia brandisiana Kurz* | 150 |
| 11 | กันเกรา | *Fagraea fragrans Roxb.* | 150 |
| 12 | กร่าง | *Ficus altissima Blume* | 150 |
| 13 | กล้วยพัด | *Ravenala madagascariensis Sonn.* | 150 |
| 14 | การะเกด | *Pandanus tectorius Parkinson ex Du Roi* | 150 |
| 15 | แก้ว | *Murraya paniculata (L.) Jack* | 150 |
| 16 | แก้วเจ้าจอม | *Guaiacum officinale L.* | 150 |
| 17 | โกงกางเขา | *Fagraea ceilanica Thunb.* | 150 |
| 18 | ขนุน | *Artocarpus heterophyllus Lam.* | 150 |
| 19 | โกสน | *Codiaeum variegatum (L.) Rumph. ex A. Juss.* | 150 |
| 20 | ข่อย | *Streblus asper Lour.* | 150 |
| 21 | ขี้เหล็ก | *Senna siamea (Lam.) H. S. Irwin & Barneby* | 150 |
| 22 | คนทีสอ | *Vitex trifolia L. subsp. trifolia* | 150 |
| 23 | คนทีเขมา | *Vitex negundo L.* | 150 |
| 24 | คริสติน่า | *Syzygium australe (J.C.Wendl. ex Link) B.Hyland* | 150 |
| 25 | แคบ้าน | *Sesbania grandiflora (L.) Poir.* | 150 |
| 26 | แคฝรั่ง | *Gliricidia sepium (Jacq.) Walp.* | 150 |
| 27 | แคแสด | *Spathodea campanulata P. Beauv.* | 150 |
| 28 | จั๋งญี่ปุ่น | *Rhapis excelsa (Thunb.) Henry* | 150 |
| 29 | จิกสวน | *Barringtonia racemosa (L.) Spreng.* | 150 |
| 30 | จันทน์ผา | *Dracaena cochinchinensis (Lour.) S. C. Chen* | 150 |
| 31 | จำปี | *Magnolia ×alba (DC.) Figlar* | 150 |
| 32 | จามจุรี | *Albizia saman (Jacq.) Merr.* | 150 |
| 33 | ชงโค | *Bauhinia purpurea L.* | 150 |
| 34 | ชบา | *Hibiscus rosa-sinensis L.* | 150 |
| 35 | ชมพูพันธุ์ทิพย์ | *Tabebuia rosea (Bertol.) Bertero ex A. DC.* | 150 |
| 36 | ชมพู่ม่าเหมี่ยว | *Syzygium malaccense (L.) Merr. & L. M. Perry* | 150 |
| 37 | ช้องนาง | *Thunbergia erecta (Benth.) T. Anderson* | 150 |
| 38 | ชะมวง | *Garcinia cowa Roxb. ex Choisy* | 150 |
| 39 | ชาฮกเกี้ยน | *Ehretia microphylla Lam.* | 150 |
| 40 | ชำมะเลียง | *Lepisanthes fruticosa (Roxb.) Leenh.* | 150 |
| 41 | เชอร์รี่ไทย | *Malpighia glabra L.* | 150 |
| 42 | ต้อยติ่ง | *Ruellia tuberosa L.* | 150 |
| 43 | ตะขบฝรั่ง | *Muntingia calabura L.* | 150 |
| 44 | ตะเคียนทอง | *Hopea odorata Roxb.* | 150 |
| 45 | ตะลิงปลิง | *Averrhoa bilimbi L.* | 150 |
| 46 | ตาล | *Borassus flabellifer L.* | 150 |
| 47 | ตาลฟ้า | *Bismarckia nobilis Hildebr. & H. Wendl.* | 150 |
| 48 | ตีนเป็ดน้ำ | *Cerbera odollam Gaertn.* | 150 |
| 49 | เต่าร้าง | *Caryota mitis Lour.* | 150 |
| 50 | ทับทิม | *Punica granatum L. var. granatum* | 150 |
| 51 | ทองกวาว | *Butea monosperma (Lam.) Taub.* | 150 |
| 52 | ทองหลางลาย | *Erythrina variegata L.* | 150 |
| 53 | ทองอุไร | *Tecoma stans (L.) Juss. ex Kunth* | 150 |
| 54 | เทียนหยด | *Duranta erecta L.* | 150 |
| 55 | ไทรทอง | *Ficus microcarpa L. f.* | 150 |
| 56 | ไทรย้อยใบแหลม | *Ficus benjamina L.* | 150 |
| 57 | ธรรมรักษา | *Heliconia psittacorum L. f.* | 150 |
| 58 | นนทรี | *Peltophorum pterocarpum (DC.) Backer ex K. Heyne* | 150 |
| 59 | น้อยหน่า | *Annona squamosa L.* | 150 |
| 60 | นีออน | *Leucophyllum frutescens (Berland.) I. M. Johnst.* | 150 |
| 61 | บานบุรี | *Cascabela thevetia (L.) Lippold* | 150 |
| 62 | บุนนาค | *Mesua ferrea L.* | 150 |
| 63 | บุหงาส่าหรี | *Citharexylum spinosum L.* | 150 |
| 64 | บาหยา | *Asystasia gangetica (L.) T. Anderson subsp. gangetica* | 150 |
| 65 | ใบเงิน ใบทอง | *Graptophyllum pictum (L.) Griff.* | 150 |
| 66 | ปรงญี่ปุ่น | *Cycas revoluta Thunb.* | 150 |
| 67 | ประดู่บ้าน | *Pterocarpus indicus Willd.* | 150 |
| 68 | ปาล์มจีบ | *Licuala grandis H. Wendl.* | 150 |
| 69 | ปาล์มชวา | *Saribus rotundifolius (Lam.) Blume* | 150 |
| 70 | ประเดหวี | *Dracaena fragrans (L.) Ker Gawl.* | 150 |
| 71 | ปาล์มน้ำมัน | *Elaeis guineensis Jacq.* | 150 |
| 72 | ปาล์มสามทาง | *Dypsis lutescens (H. Wendl.) Beentje & J. Dransf.* | 150 |
| 73 | ปาล์มหางกระรอก | *Wodyetia bifurcata A. K. Irvine* | 150 |
| 74 | ปีบ | *Millingtonia hortensis L. f.* | 150 |
| 75 | แปรงล้างขวด | *Callistemon lanceolatus (Sm.) Sweet* | 150 |
| 76 | ฝรั่ง | *Psidium guajava L.* | 150 |
| 77 | ผักหวานบ้าน | *Breynia androgyna (L.) Chakrab. & N.P. Balakr.* | 150 |
| 78 | ฝ้าย | *Gossypium herbaceum L.* | 150 |
| 79 | ไผ่ฟิลิปปินส์ | *Dracaena surculosa Lindl.* | 150 |
| 80 | พยับหมอก | *Plumbago auriculata Lam.* | 150 |
| 81 | พลับพลึงตีนเป็ด | *Hymenocallis littoralis (Jacq.) Salisb.* | 150 |
| 82 | พวงทองต้น | *Galphimia gracilis Bartl.* | 150 |
| 83 | พะยูง | *Dalbergia cochinchinensis Pierre* | 150 |
| 84 | พิกุล | *Mimusops elengi L.* | 150 |
| 85 | พุดจีบ | *Tabernaemontana divaricata (L.) R. Br.ex Roem. & Schult.* | 150 |
| 86 | พุดซ้อน | *Gardenia jasminoides J. Ellis* | 150 |
| 87 | พุดพิชญา | *Wrightia antidysenterica (L.) R. Br.* | 150 |
| 88 | พุดศุภโชค (พุดซ้อน) | *Gardenia jasminoides J. Ellis* | 150 |
| 89 | พุดสามสี | *Brunfelsia uniflora (Pohl) D. Don* | 150 |
| 90 | พุทธรักษา | *Canna indica L.* | 150 |
| 91 | เพกา | *Oroxylum indicum (L.) Benth. ex Kurz* | 150 |
| 92 | โพขี้นก | *Ficus rumphii Blume* | 150 |
| 93 | โพศรีมหาโพธิ | *Ficus religiosa L.* | 150 |
| 94 | มะกรูด | *Citrus hystrix DC.* | 150 |
| 95 | มะขาม | *Tamarindus indica L.* | 150 |
| 96 | มะขามเทศ | *Pithecellobium dulce (Roxb.) Benth.* | 150 |
| 97 | มะพร้าว | *Cocos nucifera L.* | 150 |
| 98 | มะเฟือง | *Averrhoa carambola L.* | 150 |
| 99 | มะตาด | *Dillenia indica L.* | 150 |
| 100 | มะตูม | *Aegle marmelos (L.) Corrêa ex Roxb.* | 150 |
| 101 | มะม่วง | *Mangifera indica L.* | 150 |
| 102 | มะม่วงหิมพานต์ | *Anacardium occidentale L.* | 150 |
| 103 | มะยม | *Phyllanthus acidus (L.) Skeels* | 150 |
| 104 | มะยงชิด | *Bouea oppositifolia (Roxb.) Meisn.* | 150 |
| 105 | มะละกอ | *Carica papaya L.* | 150 |
| 106 | มะลิลา | *Jasminum sambac (L.) Aiton* | 150 |
| 107 | มะรุม | *Moringa oleifera Lam.* | 150 |
| 108 | มะฮอกกานีใบใหญ่ | *Swietenia macrophylla King* | 150 |
| 109 | มันปู | *Glochidion littorale Blume* | 150 |
| 110 | มิกกี้เมาส์ | *Ochna thomasiana Engl. & Gilg* | 150 |
| 111 | โมกบ้าน | *Wrightia religiosa (Teijsm. & Binn.) Benth. ex Kurz* | 150 |
| 112 | ยางอินเดีย | *Ficus elastica Roxb. ex Hornem* | 150 |
| 113 | ยอ | *Morinda citrifolia L.* | 150 |
| 114 | ยางนา | *Dipterocarpus alatus Roxb. ex G. Don* | 150 |
| 115 | ยี่โถ | *Nerium oleander L.* | 150 |
| 116 | รัก | *Calotropis gigantea (L.) W. T. Aiton* | 150 |
| 117 | ราชพฤกษ์ | *Cassia fistula L.* | 150 |
| 118 | ราชาวดี | *Buddleja paniculata Wall.* | 150 |
| 119 | รำเพย | *Cascabela thevetia (L.) Lippold* | 150 |
| 120 | ละมุด | *Manilkara zapota (L.) P. Royen* | 150 |
| 121 | ลั่นทมแดง | *Plumeria rubra L.* | 150 |
| 122 | ลิ้นกระบือ | *Excoecaria cochinchinensis Lour. var. cochinchinensis* | 150 |
| 123 | เล็บมือนาง | *Combretum indicum (L.) De Filipps* | 150 |
| 124 | ว่านธรณีสาร | *Phyllanthus pulcher Wall. ex Müll. Arg.* | 150 |
| 125 | ว่านเพชรหึง | *Grammatophyllum speciosum Blume* | 150 |
| 126 | สบู่ดำ | *Jatropha curcas L.* | 150 |
| 127 | ส้มโอ | *Citrus maxima (Burm.) Merr.* | 150 |
| 128 | สัก | *Tectona grandis L. f.* | 150 |
| 129 | สะเดา | *Azadirachta indica A. Juss.* | 150 |
| 130 | สัตบรรณ | *Alstonia scholaris (L.) R. Br.* | 150 |
| 131 | สาละลังกา | *Couroupita guianensis Aubl.* | 150 |
| 132 | เสลา | *Lagerstroemia loudonii Teijsm. & Binn.* | 150 |
| 133 | ศรีตรัง | *Jacaranda obtusifolia Bonpl.* | 150 |
| 134 | หนามแดง | *Carissa carandas L.* | 150 |
| 135 | หม่อน | *Morus alba L.* | 150 |
| 136 | หว้า | *Syzygium cumini (L.) Skeels* | 150 |
| 137 | หมากนวล | *Adonidia merrillii (Becc.) Becc.* | 150 |
| 138 | หมากเหลือง | *Dypsis lutescens (H. Wendl.) Beentje & J. Dransf.* | 150 |
| 139 | หางนกยูงฝรั่ง | *Delonix regia (Bojer ex Hook.) Raf.* | 150 |
| 140 | หูกระจง | *Terminalia ivorensis A. Chev.* | 150 |
| 141 | หูกวาง | *Terminalia catappa L.* | 150 |
| 142 | หูปลาช่อน | *Acalypha hispida Burm. f.* | 150 |
| 143 | เหลืองปรีดียาธร | *Roseodendron donnell-smithii (Rose) Miranda* | 150 |
| 144 | อินทนิล | *Lagerstroemia speciosa (L.) Pers.* | 150 |
| 145 | อินทผลัม | *Phoenix dactylifera L.* | 150 |
| 146 | อโศกเซนคาเบรียล | *Monoon longifolium (Sonn.) B. Xue & R. M. K. Saunders* | 150 |
| 147 | เฮลิโคเนีย | *Heliconia rostrata Ruiz. & Pav.* | 150 |
| 148 | กุหลาบมอญ | *Rosa ×damascena Herrm.* | 149 |
| 149 | มะขวิด | *Limonia acidissima L.* | 149 |
| 150 | ส้มจี๊ด | *Citrus japonica Thunb.* | 149 |
| 151 | เหรียง | *Parkia timoriana (DC.) Merr.* | 149 |
| 152 | การะเกดหนู | *Pandanus pygmaeus Thouars* | 148 |
| 153 | ปาล์มพัด | *Pritchardia pacifica Seem. & H. Wendl.* | 148 |
| 154 | พุทธชาดก้านแดง | *Jasminum grandiflorum L.* | 148 |
| 155 | ละมุดเขมร | *Pouteria campechiana (Kunth) Baehni* | 148 |
| 156 | ประยงค์ | *Aglaia odorata Lour.* | 146 |
| 157 | แสงจันทร์ | *Pisonia grandis R. Br.* | 146 |
| 158 | สนประดิพัทธ์ | *Casuarina junghuhniana Miq.* | 141 |
| 159 | คัดเค้า | *Oxyceros horridus Lour.* | 137 |
| 160 | ตะโกนา | *Diospyros rhodocalyx Kurz* | 132 |
| 161 | มะกอกน้ำ | *Elaeocarpus hygrophilus Kurz* | 120 |
| 162 | ปีปทอง | *Radermachera hainanensis Merr.* | 118 |
| 163 | มะสัง | *Feroniella lucida (Scheff.) Swingle* | 111 |
| 164 | จิกนมยาน | *Barringtonia macrocarpa Hassk.* | 110 |
| 165 | สารภี | *Mammea siamensis (Miq.) T. Anderson* | 109 |
| 166 | หนวดปลาหมึกแคระ | *Schefflera arboricola (Hayata) Hayata cv. Compacta* | 108 |
| 167 | ชมนาด | *Vallaris glabra (L.) Kuntze* | 99 |
| 168 | พุดน้ำบุศย์ | *Gardenia carinata Wall. ex Roxb.* | 77 |
| 169 | ตะแบก | *Lagerstroemia floribunda Jack var. cuspidata C. B. Clarke* | 76 |
| 170 | อรพิม | *Lysiphyllum winitii (Craib) de Wit* | 69 |
| 171 | แคนา | *Dolichandrone serrulata (Wall. ex DC.) Seem.* | 67 |
| 172 | มะดัน | *Garcinia schomburgkiana Pierre* | 40 |
| 173 | ชะอม | *Senegalia pennata (L.) Willd. subsp. insuavis (Lace) I. C. Nielsen* | 34 |
| 174 | เตยหอม | *Pandanus amaryllifolius Roxb.* | 27 |
| 175 | กระดังงาสงขลา | *Cananga odorata (Lam.) Hook. f. & Thomson var. fruticosa (Craib) J. Sinclair* | 23 |
| 176 | พิลังกาสา | *Ardisia ionantha K. Larsen & C. M. Hu* | 6 |
