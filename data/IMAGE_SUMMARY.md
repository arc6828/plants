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

เป็นรายการลิงก์ข้อมูลภาพทั้งหมดที่สแกนหาได้ครั้งแรกจาก GBIF API (รวมทั้งสิ้น **408,632 ภาพ** จากพรรณไม้ **191 ชนิด**):

* **ตำแหน่งไฟล์ดิบ:** [VRU_image_links.json](VRU_image_links.json)

| ลำดับที่ | ชื่อพืชภาษาไทย | ชื่อวิทยาศาสตร์ | จำนวนรูปภาพดิบที่พบ |
| :---: | :--- | :--- | :---: |
| 1 | หม่อน | *Morus alba L.* | 21,633 |
| 2 | กระถิน | *Leucaena leucocephala (Lam.) de Wit* | 18,971 |
| 3 | มะพร้าว | *Cocos nucifera L.* | 18,928 |
| 4 | อากาเว่ | *Agave americana L.* | 16,789 |
| 5 | ยี่โถ | *Nerium oleander L.* | 16,562 |
| 6 | มะละกอ | *Carica papaya L.* | 15,171 |
| 7 | ทองอุไร | *Tecoma stans (L.) Juss. ex Kunth* | 12,751 |
| 8 | ทับทิม | *Punica granatum L. var. granatum* | 11,027 |
| 9 | ฝรั่ง | *Psidium guajava L.* | 10,546 |
| 10 | พยับหมอก | *Plumbago auriculata Lam.* | 9,974 |
| 11 | หูกวาง | *Terminalia catappa L.* | 9,673 |
| 12 | แคแสด | *Spathodea campanulata P. Beauv.* | 8,556 |
| 13 | มะม่วง | *Mangifera indica L.* | 8,303 |
| 14 | ยอ | *Morinda citrifolia L.* | 8,249 |
| 15 | สะเดา | *Azadirachta indica A. Juss.* | 7,727 |
| 16 | พุทธรักษา | *Canna indica L.* | 7,631 |
| 17 | หางนกยูงฝรั่ง | *Delonix regia (Bojer ex Hook.) Raf.* | 7,470 |
| 18 | ไทรทอง | *Ficus microcarpa L. f.* | 7,029 |
| 19 | นีออน | *Leucophyllum frutescens (Berland.) I. M. Johnst.* | 6,830 |
| 20 | รัก | *Calotropis gigantea (L.) W. T. Aiton* | 6,390 |
| 21 | แก้ว | *Murraya paniculata (L.) Jack* | 6,120 |
| 22 | บาหยา | *Asystasia gangetica (L.) T. Anderson subsp. gangetica* | 5,815 |
| 23 | เทียนหยด | *Duranta erecta L.* | 5,345 |
| 24 | ตะขบฝรั่ง | *Muntingia calabura L.* | 5,167 |
| 25 | ธรรมรักษา | *Heliconia psittacorum L. f.* | 4,957 |
| 26 | การะเกด | *Pandanus tectorius Parkinson ex Du Roi* | 4,878 |
| 27 | เฮลิโคเนีย | *Heliconia rostrata Ruiz. & Pav.* | 4,567 |
| 28 | บานบุรี | *Cascabela thevetia (L.) Lippold* | 4,562 |
| 29 | รำเพย | *Cascabela thevetia (L.) Lippold* | 4,562 |
| 30 | โพศรีมหาโพธิ | *Ficus religiosa L.* | 4,288 |
| 31 | ราชพฤกษ์ | *Cassia fistula L.* | 4,277 |
| 32 | ลั่นทมแดง | *Plumeria rubra L.* | 4,089 |
| 33 | มะขามเทศ | *Pithecellobium dulce (Roxb.) Benth.* | 4,042 |
| 34 | ลำไย | *Dimocarpus longan Lour.* | 3,619 |
| 35 | มะรุม | *Moringa oleifera Lam.* | 3,530 |
| 36 | ขนุน | *Artocarpus heterophyllus Lam.* | 3,251 |
| 37 | มะขาม | *Tamarindus indica L.* | 3,082 |
| 38 | พุดซ้อน | *Gardenia jasminoides J. Ellis* | 2,843 |
| 39 | พุดศุภโชค (พุดซ้อน) | *Gardenia jasminoides J. Ellis* | 2,843 |
| 40 | เล็บมือนาง | *Combretum indicum (L.) De Filipps* | 2,825 |
| 41 | โกสน | *Codiaeum variegatum (L.) Rumph. ex A. Juss.* | 2,722 |
| 42 | มะเฟือง | *Averrhoa carambola L.* | 2,671 |
| 43 | สัก | *Tectona grandis L. f.* | 2,526 |
| 44 | ช้องนาง | *Thunbergia erecta (Benth.) T. Anderson* | 2,516 |
| 45 | กระถินณรงค์ | *Acacia auriculiformis A. Cunn. ex Benth.* | 2,510 |
| 46 | มะม่วงหิมพานต์ | *Anacardium occidentale L.* | 2,487 |
| 47 | แคฝรั่ง | *Gliricidia sepium (Jacq.) Walp.* | 2,481 |
| 48 | หว้า | *Syzygium cumini (L.) Skeels* | 2,446 |
| 49 | กล้วย | *Musa acuminata Colla* | 2,324 |
| 50 | คนทีเขมา | *Vitex negundo L.* | 2,253 |
| 51 | อินทผลัม | *Phoenix dactylifera L.* | 2,223 |
| 52 | สาละลังกา | *Couroupita guianensis Aubl.* | 2,168 |
| 53 | ต้อยติ่ง | *Ruellia tuberosa L.* | 2,015 |
| 54 | กระทิง | *Calophyllum inophyllum L.* | 2,008 |
| 55 | ชบา | *Hibiscus rosa-sinensis L.* | 1,879 |
| 56 | อินทนิล | *Lagerstroemia speciosa (L.) Pers.* | 1,808 |
| 57 | พลับพลึงตีนเป็ด | *Hymenocallis littoralis (Jacq.) Salisb.* | 1,792 |
| 58 | ทองกวาว | *Butea monosperma (Lam.) Taub.* | 1,786 |
| 59 | จามจุรี | *Albizia saman (Jacq.) Merr.* | 1,751 |
| 60 | น้อยหน่า | *Annona squamosa L.* | 1,714 |
| 61 | ชมพูพันธุ์ทิพย์ | *Tabebuia rosea (Bertol.) Bertero ex A. DC.* | 1,705 |
| 62 | พุดจีบ | *Tabernaemontana divaricata (L.) R. Br.ex Roem. & Schult.* | 1,565 |
| 63 | ไทรย้อยใบแหลม | *Ficus benjamina L.* | 1,466 |
| 64 | หมากนวล | *Adonidia merrillii (Becc.) Becc.* | 1,421 |
| 65 | ประเดหวี | *Dracaena fragrans (L.) Ker Gawl.* | 1,408 |
| 66 | ชาฮกเกี้ยน | *Ehretia microphylla Lam.* | 1,400 |
| 67 | ชมพู่ม่าเหมี่ยว | *Syzygium malaccense (L.) Merr. & L. M. Perry* | 1,299 |
| 68 | ยางอินเดีย | *Ficus elastica Roxb. ex Hornem* | 1,295 |
| 69 | ตาล | *Borassus flabellifer L.* | 1,250 |
| 70 | หูปลาช่อน | *Acalypha hispida Burm. f.* | 1,246 |
| 71 | อโศกเซนคาเบรียล | *Monoon longifolium (Sonn.) B. Xue & R. M. K. Saunders* | 1,246 |
| 72 | ละมุด | *Manilkara zapota (L.) P. Royen* | 1,162 |
| 73 | สัตบรรณ | *Alstonia scholaris (L.) R. Br.* | 1,156 |
| 74 | นนทรี | *Peltophorum pterocarpum (DC.) Backer ex K. Heyne* | 1,148 |
| 75 | จิกสวน | *Barringtonia racemosa (L.) Spreng.* | 1,140 |
| 76 | ปาล์มสามทาง | *Dypsis lutescens (H. Wendl.) Beentje & J. Dransf.* | 1,081 |
| 77 | หมากเหลือง | *Dypsis lutescens (H. Wendl.) Beentje & J. Dransf.* | 1,081 |
| 78 | สบู่ดำ | *Jatropha curcas L.* | 1,022 |
| 79 | มะฮอกกานีใบใหญ่ | *Swietenia macrophylla King* | 965 |
| 80 | ตะลิงปลิง | *Averrhoa bilimbi L.* | 958 |
| 81 | ขี้เหล็ก | *Senna siamea (Lam.) H. S. Irwin & Barneby* | 933 |
| 82 | เชอร์รี่ไทย | *Malpighia glabra L.* | 871 |
| 83 | บุหงาส่าหรี | *Citharexylum spinosum L.* | 812 |
| 84 | เต่าร้าง | *Caryota mitis Lour.* | 753 |
| 85 | คนทีสอ | *Vitex trifolia L. subsp. trifolia* | 729 |
| 86 | ชงโค | *Bauhinia purpurea L.* | 721 |
| 87 | พิกุล | *Mimusops elengi L.* | 714 |
| 88 | แก้วเจ้าจอม | *Guaiacum officinale L.* | 709 |
| 89 | แปรงล้างขวด | *Callistemon lanceolatus (Sm.) Sweet* | 706 |
| 90 | ปาล์มน้ำมัน | *Elaeis guineensis Jacq.* | 683 |
| 91 | ยูคาลิปตัส | *Eucalyptus camaldulensis Dehnh.* | 614 |
| 92 | ปรงญี่ปุ่น | *Cycas revoluta Thunb.* | 611 |
| 93 | คริสติน่า | *Syzygium australe (J.C.Wendl. ex Link) B.Hyland* | 602 |
| 94 | ชมพู่ | *Syzygium samarangense (Blume) Merr. & L.M.Perry* | 586 |
| 95 | ตีนเป็ดน้ำ | *Cerbera odollam Gaertn.* | 552 |
| 96 | มะตาด | *Dillenia indica L.* | 519 |
| 97 | ผักหวานบ้าน | *Breynia androgyna (L.) Chakrab. & N.P. Balakr.* | 494 |
| 98 | มะยม | *Phyllanthus acidus (L.) Skeels* | 474 |
| 99 | มะตูม | *Aegle marmelos (L.) Corrêa ex Roxb.* | 468 |
| 100 | กรรณิกา | *Nyctanthes arbor-tristis L.* | 466 |
| 101 | กล้วยพัด | *Ravenala madagascariensis Sonn.* | 465 |
| 102 | ทองหลางลาย | *Erythrina variegata L.* | 454 |
| 103 | ตะขบป่า | *Flacourtia indica (Burm. f.) Merr.* | 442 |
| 104 | พวงทองต้น | *Galphimia gracilis Bartl.* | 434 |
| 105 | มะลิลา | *Jasminum sambac (L.) Aiton* | 427 |
| 106 | จั๋งญี่ปุ่น | *Rhapis excelsa (Thunb.) Henry* | 396 |
| 107 | ปีบ | *Millingtonia hortensis L. f.* | 389 |
| 108 | เหลืองปรีดียาธร | *Roseodendron donnell-smithii (Rose) Miranda* | 354 |
| 109 | ส้มโอ | *Citrus maxima (Burm.) Merr.* | 331 |
| 110 | เฟื่องฟ้า | *Bougainvillea spectabilis Willd.* | 323 |
| 111 | มิกกี้เมาส์ | *Ochna thomasiana Engl. & Gilg* | 315 |
| 112 | ประดู่บ้าน | *Pterocarpus indicus Willd.* | 305 |
| 113 | กะตังใบ | *Leea indica (Burm. f.) Merr.* | 288 |
| 114 | ปาล์มหางกระรอก | *Wodyetia bifurcata A. K. Irvine* | 277 |
| 115 | ฝ้าย | *Gossypium herbaceum L.* | 270 |
| 116 | เข็ม | *Ixora coccinea L.* | 264 |
| 117 | เพกา | *Oroxylum indicum (L.) Benth. ex Kurz* | 256 |
| 118 | แคบ้าน | *Sesbania grandiflora (L.) Poir.* | 244 |
| 119 | โพขี้นก | *Ficus rumphii Blume* | 239 |
| 120 | ตาลฟ้า | *Bismarckia nobilis Hildebr. & H. Wendl.* | 235 |
| 121 | ใบเงิน ใบทอง | *Graptophyllum pictum (L.) Griff.* | 219 |
| 122 | พุดพิชญา | *Wrightia antidysenterica (L.) R. Br.* | 213 |
| 123 | ปาล์มจีบ | *Licuala grandis H. Wendl.* | 212 |
| 124 | สนมังกร | *Juniperus chinensis L.* | 205 |
| 125 | พุดสามสี | *Brunfelsia uniflora (Pohl) D. Don* | 199 |
| 126 | กร่าง | *Ficus altissima Blume* | 193 |
| 127 | หนามแดง | *Carissa carandas L.* | 185 |
| 128 | ปาล์มสิบสองปันนา | *Phoenix roebelenii O’Brien* | 174 |
| 129 | ปาล์มสิบสองปันนา | *phoenix roebelenii O'Brien* | 174 |
| 130 | ข่อย | *Streblus asper Lour.* | 168 |
| 131 | ว่านเพชรหึง | *Grammatophyllum speciosum Blume* | 153 |
| 132 | บุนนาค | *Mesua ferrea L.* | 148 |
| 133 | กันเกรา | *Fagraea fragrans Roxb.* | 145 |
| 134 | โมกบ้าน | *Wrightia religiosa (Teijsm. & Binn.) Benth. ex Kurz* | 143 |
| 135 | มะกรูด | *Citrus hystrix DC.* | 139 |
| 136 | มะนาว | *Citrus aurantiifolia (Christm.) Swingle* | 139 |
| 137 | มะขวิด | *Limonia acidissima L.* | 136 |
| 138 | ละมุดเขมร | *Pouteria campechiana (Kunth) Baehni* | 129 |
| 139 | ไผ่ฟิลิปปินส์ | *Dracaena surculosa Lindl.* | 124 |
| 140 | ลิ้นกระบือ | *Excoecaria cochinchinensis Lour. var. cochinchinensis* | 112 |
| 141 | ปาล์มพัด | *Pritchardia pacifica Seem. & H. Wendl.* | 111 |
| 142 | ปาล์มชวา | *Saribus rotundifolius (Lam.) Blume* | 107 |
| 143 | ไผ่ | *Bambusa vulgaris Schrad.* | 106 |
| 144 | ไผ่น้ำเต้า | *Bambusa vulgaris Schrad.* | 106 |
| 145 | จันทน์ผา | *Dracaena cochinchinensis (Lour.) S. C. Chen* | 104 |
| 146 | โกงกางเขา | *Fagraea ceilanica Thunb.* | 97 |
| 147 | กระท้อน | *Sandoricum koetjape (Burm. f.) Merr.* | 91 |
| 148 | จำปี | *Magnolia ×alba (DC.) Figlar* | 91 |
| 149 | ประยงค์ | *Aglaia odorata Lour.* | 90 |
| 150 | กระดังงาจีน | *Artabotrys hexapetalus (L. f.) Bhandari* | 84 |
| 151 | พุทธชาดก้านแดง | *Jasminum grandiflorum L.* | 75 |
| 152 | ส้มจี๊ด | *Citrus japonica Thunb.* | 72 |
| 153 | มันปู | *Glochidion littorale Blume* | 47 |
| 154 | สนประดิพัทธ์ | *Casuarina junghuhniana Miq.* | 44 |
| 155 | พะยอม | *Shorea roxburghii G.Don* | 43 |
| 156 | กุหลาบมอญ | *Rosa ×damascena Herrm.* | 38 |
| 157 | ตะเคียนทอง | *Hopea odorata Roxb.* | 35 |
| 158 | ว่านธรณีสาร | *Phyllanthus pulcher Wall. ex Müll. Arg.* | 33 |
| 159 | หมากเขียว | *Ptychosperma macarthurii (H.Wendl. ex T.Moore) H.Wendl. ex Dykes* | 32 |
| 160 | หนวดปลาหมึกแคระ | *Schefflera arboricola (Hayata) Hayata cv. Compacta* | 28 |
| 161 | พุดน้ำบุศย์ | *Gardenia carinata Wall. ex Roxb.* | 22 |
| 162 | แคนา | *Dolichandrone serrulata (Wall. ex DC.) Seem.* | 19 |
| 163 | ปีปทอง | *Radermachera hainanensis Merr.* | 15 |
| 164 | การะเกดหนู | *Pandanus pygmaeus Thouars* | 11 |
| 165 | ชมนาด | *Vallaris glabra (L.) Kuntze* | 11 |
| 166 | ศรีตรัง | *Jacaranda obtusifolia Bonpl.* | 10 |
| 167 | สารภี | *Mammea siamensis (Miq.) T. Anderson* | 10 |
| 168 | กระดังงาสงขลา | *Cananga odorata (Lam.) Hook. f. & Thomson var. fruticosa (Craib) J. Sinclair* | 9 |
| 169 | มะยงชิด | *Bouea oppositifolia (Roxb.) Meisn.* | 9 |
| 170 | แสงจันทร์ | *Pisonia grandis R. Br.* | 9 |
| 171 | หูกระจง | *Terminalia ivorensis A. Chev.* | 8 |
| 172 | อรพิม | *Lysiphyllum winitii (Craib) de Wit* | 8 |
| 173 | เสลา | *Lagerstroemia loudonii Teijsm. & Binn.* | 7 |
| 174 | กระพี้จั่น | *Millettia brandisiana Kurz* | 6 |
| 175 | ชะมวง | *Garcinia cowa Roxb. ex Choisy* | 6 |
| 176 | คัดเค้า | *Oxyceros horridus Lour.* | 5 |
| 177 | มะกอกน้ำ | *Elaeocarpus hygrophilus Kurz* | 4 |
| 178 | มะดัน | *Garcinia schomburgkiana Pierre* | 4 |
| 179 | ราชาวดี | *Buddleja paniculata Wall.* | 4 |
| 180 | จิกนมยาน | *Barringtonia macrocarpa Hassk.* | 3 |
| 181 | ตะโกนา | *Diospyros rhodocalyx Kurz* | 3 |
| 182 | เหรียง | *Parkia timoriana (DC.) Merr.* | 3 |
| 183 | กระทุ่มนา | *Mitragyna diversifolia (Wall. ex G. Don) Havil.* | 2 |
| 184 | ชำมะเลียง | *Lepisanthes fruticosa (Roxb.) Leenh.* | 2 |
| 185 | พะยูง | *Dalbergia cochinchinensis Pierre* | 2 |
| 186 | มะสัง | *Feroniella lucida (Scheff.) Swingle* | 2 |
| 187 | ยางนา | *Dipterocarpus alatus Roxb. ex G. Don* | 2 |
| 188 | ชะอม | *Senegalia pennata (L.) Willd. subsp. insuavis (Lace) I. C. Nielsen* | 1 |
| 189 | ตะแบก | *Lagerstroemia floribunda Jack var. cuspidata C. B. Clarke* | 0 |
| 190 | พิลังกาสา | *Ardisia ionantha K. Larsen & C. M. Hu* | 0 |
| 191 | เตยหอม | *Pandanus amaryllifolius Roxb.* | 0 |
