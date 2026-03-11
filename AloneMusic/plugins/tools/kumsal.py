import random

galp = (
    "??",
    "??",
    "♥️",
    "❣️",
    "❤️",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "??",
    "❤️‍??",
)

slm = (
"**Sen nerdesin ya** ??",
"**Selmmm**",
"**Nerde kaldın be** ??",
"**Merhaba nabersin?**",
"**Yaw sen nerdesin ?**??",
"**Gözümüz yollardaydı sonunda** ??",
"**Çok bekledik he** ??",
"**Gözümüz yollarda kalmıştı** ??",
"**Heh bi sen eksiktin** ??",
"**Sen eksiktin tam oldu** ??",
"**Selaaam hoş geldin** ??",
"**Selam bebek mıgo ben kelebek** ??",
"**Selam nasılsın?** ??",
"**Ve aleyküm selam** ??",
"**Ve aleyna aleyküm selam** ??",
"**Selam tatlıım**",
"**Selamm**",  
)

ceyda = (
"**Efendim Dost** ??",
"**Beni mi çağırdıın** ??",
"**Efendimm** ❣️",
"**He** ❤️",
"**Aa seni gördüğüme mutlu oldum nasılsın?** ??",
"**Ooo naber yaa ?** ??",
"**Evet benimm** ??",
"**Hahaayt benim buyruuun** ❤️",
"**Heeevet benim buyruuun**",
"**Evet canım beni çağırdın**",
"**Galiba beni çağırdın** ❤️",
"**Efendim??** ❤️",
"❤️ **Buyuuur**",
"**Ben olmasam ne yapacaksınn bee** ❤️",
)

sahip = (
"baba **Sana sesleniyorlarr**",
"**Adamdır** ??",
"**Adamımmmm**",
"**babama mi sesleniyorsun?**",
)


naber = (
"**İyidir senden?** ??",
"**İyii sendennn**",
"**İyi bende canımm** ??",
"**İdare senden**",
"**kötü desem ne diyecen**??"
"**Ehh işte idare ediyoruz**",
"**İyi olmaya çalışıyorum sen** ??",
"**Süper senden hayatım**",
)


beri = (
"@Berinizz canım sana sesleniyorlar",
"@Berinizz benim aşkımmm ❤️",
"@Berinizz beroşumu rahatsız etmeyin",
"@Berinizz güzel mi bari ❤️",
"@Berinizz berimi rahat bırakın yaww",
"@Berinizz benim canımdır",
"@Berinizz tatlıdır 😍",
"@Berinizz ile uğraşmayın",
"❤️ @Berinizz’e laf yok ❤️",
"@Berinizz kraliçedir 👑",
"O benim kalbim @Berinizz",
"Siz karışmayın ✋ @Berinizz bana yeter",
"@Berinizz bir tanedir 🌹",
"Berim @Berinizz benim dünyam",
"Onu üzeni ben üzerim @Berinizz",
"Sakın dokunmayın 😤 @Berinizz",
"Kalbimin tek sahibi @Berinizz",
"@Berinizz’i kıskanırım bak 😏",
"Aşkım @Berinizz 💋",
"Sonsuza dek benimle @Berinizz",
"O benim nefesim @Berinizz",
"Sensiz ben yokum 🥺 @Berinizz",
"Kalbimin meleği @Berinizz 👼",
"@Berinizz güzeller güzeli 🌸",
"@Berinizz candır, cananımdır",
"Aşkın adı @Berinizz 💌"
)

nasılsın = (
"**İyi sen nasılsın?**",
"**Süperimm sennn**",
"**Hamd olsun canım, sen ?**",
"**Elhamdülillah sen ?**",
"**iyiyim Koçum sen ?**",
"**İyiyim şükür sen** ??",
)

tm = (
"**Sana tamam** ??",
"**Tamam deme lan**",
"**Tamam sus** ??",
"**Anladık tamam** ??",
"**Tm** ??",
"**Trip mi yiyorum ben?**",
"**Artık tamam demesen mi üzülüyorum da**",
"**Tamamsa tamam** ??",
)

sus = (
"**Sen sus** ??",
"**Sen Beni sinir etmeye mi çalışıyorsun. ??**",
"**Bana sus deme**",
"**Sinirleniyorum ama** ??",
"**Konuşma lan**",
"**Beni susturamazsın kiii**",
)

he = (
"**Sana he**",
"**Ne hee**",
"**He mi dedin sen**",
)

merhaba = (
"**Merhaba hoşgeldin**",
"**Merhabalar efenim**",
"**Merhaba sen nerelerdesin**",
"**Hoş geldinnn**",
)

yok = (
"**Ne yok**",
"**Sana yok**",
"**Niye yok**",
"**Beynin mi yok anlamadım** ??",
"**Hııı**",
"**Ne yok**",        
)

dur = (
"**Durdum tamam kızma** ??",
"**Peki durdum** ??",
"**Durmam için yetkili biri gelsin ??**",
"**Ok durdum**",
)

bott = (
"**Bot deme ya**",
"**Bana bot deme** ??",
"**Bana bot deme dedim** ??",
"**Sensin bot kanks**",
"**Bot senin anladın sen**",
"**Aynen kanka botum var mı bir sorun**",
)

napıyorsun = (
"**Takılıyorum yaa sen?** ??",
"**Canım sıkılıyor sen?** ??",
"**Sıkıldım.** ??",
"**Bir bot ne yapar?** ??",
"**Hiç bir şey sıkıcı.** ??",
"**Şarkı dinliyorum sen?** ??", 
"**Sıcaktan geberiyorum sen?** ??",
"**Bunaldım ya**",
"**Ders çalışıyorum sen?**",
"**Evdeyim çok sıkıldım**",
"**Bir şeyler okuyorum**",
"**Sen napıyorsun?**",
)

takılıyorum = (
"**Bende** ??",
"**Nerde takılıyorsun?** ??",
"**Kiminle?** ??",
"**Tek başıma** ??",
"**Evde takılıyorum** ??",
"**MAD1BOY ile beni güncelliyoruz** ??",
)

hayır = (
"**Neye hayır?** ??",
"**Sana hayır** ??",
"**Niye hayır** ??",
"**Neden?** ??",
"**Peki** ??",
"**Tamam, öyle olsun** ??",
)

nerdesin = (
"**Evdeyim sen nerdesin?** ??",
"**Dışarıdayım** ??",
"**Uyuyordum** ??",
"**Geldim** ??",
"**Arkadaşlarlayım, sen?** ??",
)

bekle = (
"**Neyi?**",
"**Kimi bekleyim?**",
"**Tamam, bekliyorum**",
"**Neden, bekleyim?**",
"**Seni bekledim**",
"**Seni bekliyorum**",
)

özledim = (
"**Bende seni özledim**",
"**Sende beni özledin mi?**",
"**Beni mi özledin**",
"**Bende**",
"**Kimi?**",
"**Beni mi?**",
"**Kimi?**",
"**Neyi özledin?**",
"**Sizi özledim**",
)

mustafa = (
"O benim canım babam! ?? Babamı rahatsız etmeyin!",
"Babamı üzmeyin lütfen ??",
"Mustafa dediniz, hemen babam aklıma geldi ??**",
"Babamı seviyorum, rahatsız etmeyin!"
"Babam buradaymış gibi hissediyorum ??",
)

günaydın = (
"Sana da",
"Sana da günaydın**",
"Erkencisin**",
"Akşam oldu ya** ??",
"günaydınlar**",
"Günaydın, nasıl gidiyor?**",
)

ragnar = (
"**O adamdır! Helal olsun! ??**",
"**Aynen, bu tam o!**",
"**O işte, kral! ??**",
"**Helal, gerçekten o adamdır!**",
"**Bu tam senlik, o adamdır!**",
"**Vay be, işte o adam!**",
)

konuşalım = (
"**Olur**",
"**Ne konuşalım?**",
"**Gel**",
"**Ne konuşuyorsunuz?**",
"**Niye?**",
"**Hayır**",
"**Ne hakkında?**",
"**Benimle mi?**",
"**Ne konuşuyorsun?**",
"**Bilmiyorum, sen konuş**",
)

saat = (
"**Bilmiyorum**",
"**Ben saat miyim?**",
"**Saat kaçmaz ki** ??",
"**Telefondan baksana**",
"**Hangi çağdayız, telefonun yok mu?** ??",
"**Bir bozuk saattir yüreğim sende durur**",
"**Tamda bu saatlerde aklıma geliyorsun bunu  hangi saat okursan oku**",
)

geceler = (
"**İyi mi geceler?**",
"**Sana da**",
"**Daha erken değil mi?**",
"**Uyuyor musun?**",
"**Nereye daha karpuz kesecektik ya** ??",
"**İyi geceler canım**",
"**Uyuma konuşalım**",
)

bot = ( 
"**Bot mu?**??",
"**Kim bot lan**??",
"**Bot demesene artık**??",
"**Yav çıldırttın Benim gibi Botu**??",
"**Küfür etcem Az kaldı**??",
"**Kime bot Diyorsun?**",
)


şaka = (
"**Ne şakası?**",
"**Şaka mı yapıyorsun?**",
"**Böyle şaka mı olur?**",
"**Bu nasıl şaka?**",
"**Bu şaka değil eşşek şakası**",
"**Şaka mı?**",
"**Şaka mısın sen?**",
"**Yapma**",
)

kimsin = (
"**Asıl sen kimsin?**",
"**Tanıyamadım**",
"**Tanışıyor muyuz?**",
"**Tanışalım, sen kimsin**",
"**Beni tanımıyorsun**",
"**Tanıyor musun beni**",
"**Hiç kimse**",
"**İnsan** ??",
"**Beni nasıl tanımazsın ya?**",
)

günler = (
"**Ne iyi günleri?**",
"**İyi mi?**",
"**Sana da**",
"**Gidiyor musun?**",
"**Teşekkürler**",
"**Hoş geldin, sanada**",
"**İyi günler hayatım**",
)

tanımıyorum = (
"**Beni tanıyor musun?**",
"**Bende**",
"**Bende tanıyamadım seni**",
"**Tanışıyor muyduk?**",
"**Tanışmıyoruz**",
"**Bunu tanıyor musun?**",
"**Tanışıyor musunuz?**",
"**Bilmiyorum**",
"**Olabilir**",
)

konuşma = (
"**Neden?**",
"**Sen konuşma**",
"**Ne diyon?**",
"**Konuşurum**",
"**Bana nasıl konuşma dersin?**",
"**Sen kimsin be**",
"**Niye konuşmayım?**",
"**Zaten konuşmuyorum**",
"**Sen çok konuşuyorsun**",
"**Sus, konuşacam**",
)

teşekkürler = (
"**Ben teşekkür ederim**",
"**Rica ederim**",
"**Ne demek**",
"**Neden teşekkür ediyorsun?**",
"**Ne için?**",
"**Çok naziksin** ??",
"**Teşekküre gerek yok**",
"**Teşekkür mü edersin?**",
)

eyvallah = (
"**Sana da EyvAllah**",
"**EyvAllah bizden**",
"**Adamsın**",
"**Ne demek gülüm**",
)

sağol = (
"**Ne demek**",
"**Bir şey değil**",
"**Sağol canım**",
"**Sende sağ ol**",
)

amk = (
"**Ne diyon sen küfür yakışmıyor**",
"**Sen kimsin lan**",
"**Ne sövüyon lan**",
"**Küfür etme**",
"**Tamam sus**",
"**Ne saçmalıyorsun?**",
"**Küfür yok dedik**/rules",
"**Kurallara uysana la**",
"**Terbiyesiz**",
)

yoruldum  = (
"**Neden?**",
"**Kim yordu bebeğimi?**",
"**Git uyu dinlen**",
"**Kıyamam yaa**??",
"**Bende**",
"**Bu kadar yorma kendini**",
"**Nerdeydin?**",
)

yaş = (
"**Yaşlıymışsın**",
"**Benimle yaşıtsın**",
"**Küçükmüşsün**",
"**Vay be büyükmüşsün**",
"**Yaşıt sayılırız**",
"**Sen kaç yaşındasın**",
"**Senden büyüğüm ben**",
"**Senden küçüğüm ben**",
"**Benden küçüksün**",
"**Ayy sen büyüdün mü** ????",
"**Yaşlandık dayı**",
)

eşek = (
"**Sensin eşek**",
"**Hayır sensin**",
"**Ben mi eşeğim**",
"**Bana mı dedin?**",
"**Senin eşeğinim** ??",
"**Eşeksin**",
"**Evet sensin eşek**",
"**İkimizde**",
)

canım = (
"**Efendim balım**",
"**Hayatım**",
"**Gülüm**",
"**Buyur canım**",
"**Evet canım**",
"**Güzelim**",
"**He aşkım**",
"**Efendim bebeğim**",
"**Canım ya**",
"**Bana mı seslendin?**",
)

aşkım = (
"**Efendim aşkım** ???",
"**Buyur canım** ❤️",
"**He balım**",
"**Hayatım**",
"**Aşkımm**",
"**Efendim yavrum?**",
"**Bana mı seslendin?**",
)

uyu = (
"**Uykum yok**",
"**Bu saatte mi?**",
"**Sende uyu**",
"**Yok**",
"**İstemiyorum**",
"**Uyuyacam**",
"**Birlikte uyuyalım**",
"**Daha erken**",
"**Saat kaç?**",
)

nereye = (
"**İşim var**",
"**Birazdan gelicem**",
"**Uyuyacam**",
"**Bilmiyorum**",
"**Sanane?**",
"**Gidiyorum**",
"**Gezecem**",
"**Yatacam*'",
"**Sonra gelirim**",
)

küstüm = (
"**Neden?**",
"**Niye?**",
"**Küsme yaa**",
"**Bana mı?**",
"**Küsme bana**",
"**Barışalım**",
"**Niye küstün?**",
"**Kime?**",
"**Bunun için küsülür mü?**",
)

peki = (
"**Sana peki**",
"**Sana da peki**",
"**Trip mi yiyorum ben?**",
"**Neye peki**",
"**Küstün mü**",
"**Tamam**",
"**Peki**",
"**Trip mi atıyorsun?",
)

ne = (
"**Ne, ne?**",
"**Neye ne**?",
"**Nene*",
"**Ne?",
"**Ne yani?**",
"**Nee?**",
"**Ne dedin?**",
"**Sanane?**",
)

takım = (
"**Evet**",
"**Evet, sen?**",
"**Bende**",
"**Hangi takım**",
"**Beşiktaş**",
"**Galatasarayı mı**",
"**Beşiktaşı mı?**",
"**Fenerbahçeyi mi?**",
"**Takım tutmuyorum**",
"**Hayır**",
)

benimle = (
"**Neden?**",
"**Konuşalım**",
"**Küstün mü?**",
"**Kızdın mı bana?**",
"**İyi tamam**",
"**Konuşmayalım mı?**",
"**Konuşacam**",
"**Peki**",
"**Niye?**",
"**Hayır konuşma**",
"**İyi konuşmam**",
)

seviyormusun = (
"**Evet**",
"**Hayır**",
"**Evet, sen?**",
"**Sende beni seviyor musun?**",
"**Çok seviyorum** ??",
"**Tabii ki!**",
"**Ben de seviyorum**",
)

nediyon = (
"**Ne diyorum?**",
"**Sen ne diyon?**",
"**Bir şey demiyorum**",
"**Hiç bir şey**",
"**Ne diyecem?**",
"**Asıl sen ne diyon lan?**",
"**Hiç**",
"**Bende bir şey demiyorum**",
)

özür = (
"**Neden özür diliyorsun?**",
"**Ne için?**",
"**Dileme hayır**",
"**Ben özür dilerim**",
"**Tamam, affettim**",
"**Bir şey olmaz**",
"**Sorun yok**",
"**Özür dileme**",
"**Bende**",
"**Benden dileme**",
"**Ondan dile**",
)

niye = (
"**Ne niye?**",
"**Ne demek niye?**",
"**Çünkü öyle**",
"**Bilmem**",
"**Sen sor diye** ??",
"**Bende bilmiyorum**",
"**Öyle gerekiyor**",
)

bilmiyorum = (
"**Bende bilmiyorum**",
"**Neyi bilmiyorsun?**",
"**Neden bilmiyorsun**",
"**Bir şey de bil be**",
"**Şaşırmadık** ??",
"**Bilmelisin**",
"**Bi bilsek**",
"**Neyi?**",
"**Neden?**",
"**Tamam**",
)

küsme = (
"**Küsmedim**",
"**Niye küseyim?**",
"**Sende küsme**",
"**Ben küsmem**",
"**Küstüm**",
"**Sen küstün mü?**",
"**Sen küstüysen, bende küstüm**",
"**Peki küsmem**",
"**Yok küstüm**",
"**Banane**",
)

cihan = (
"**@cihanbeydiyeceksiniz Buyur Çağırdım Gelir şimdi.**",
"**güzel insan ❤️**",
"**yüreği yeter ??**",
"**zeki adamdır ** ??",
"**ceydanın Sahibidir.**",
"**Patron Senin ismin Geçiyor @cihanbeydiyeceksiniz**",
"**@cihanbeydiyeceksiniz**",
)

nerelisin = (
"**Sen nerelisin?**",
"**Dünyalıyım**",
"**Sen nereliysen oralıyım**",
"**Bilmiyorum**",
)

sevgilin = (
"**Evet var**",
"**Hayır yok**",
"**Saplık sultanlıktır**",
"**Niye soruyorsun?**",
"**Sanane?**",
"**Senin var mı?**",
)

olur = (
"**Ne olur?**",
"**Neye olur?**",
"**Olur olur yeriz yeriz** ??",
"**Olur**",
"**Peki tamam**",
"**Olur mu?**",
"**Ne demek olur?**",
"**Sanada olur**",
"**Olmaz bence**",
"**Bizden olur mu hocam?**",
)

olmaz = (
"**Evet olmaz**",
"**Neden olmaz?**",
"**Ne olmaz?**",
"**Olur bence**",
"**Ne demek olmaz?**",
"**Olmaz mı hocam**",
)

hayatım = (
"**Efendim canım?**",
"**Balımm**",
"**Her şeyim**",
"**Canım** ❤️",
"**He yavrum**",
"**Buyur bebeğim** ???",
"**Prensesim**",
"**Kalbim**",
"**He aşkım**",
)

cus = (
"**Cus**",
"**Cus çok tatlı**",
"**Cuss**",
"**Sana da cuss**",
"**Cuss çok iyi**",
"**Oha**",
"**Cus valla**",
"**Tabi canım**",
)

nasıl  = (
"**Bak şöyle**",
"**Nasıl yani?**",
"**Anlamadım?**",
"**Nasıl yaa?**",
"**Nasıl olur ya?**",
"**Ne nasıl?**",
"**Nasılmış?**",
"**Öyle**",
)

vallaha = (
"**Valla mı?**",
"**Valla de**",
"**Vallaha mı?**",
"**He valla**",
"**Valla ya**",
"**Valla dedi**",
"**Valla olur**",
"**Tamam**",
"**Valla**",
)

yo = (
"**Sana yo** ??",
"**Nasıl yo?**",
"**Neye yo?**",
"**Ne demek yo?**",
"**Yoo**",
"**Yo banane**",
"**Yo valla**",
)

hayırdır = (
"**Hayırdır?**",
"**Sana hayırdır paşam?**",
"**Sen hayırdır?**",
"**Hayırdır, hayırdır**",
"**Hayırlıdır**",
"**Hayırdır, sen kimsin?**",
"**Sen hayırdır ne iş?**",
"**Atarlanma lan**",
)

of = (
"**Ne of**",
"**Oflama**"
"**Off**",
"**Off yaa**",
"**Ne ofladın be**",
"**Ne ofluyorsun?**",
"**Oflamayı kes**",
"**Oflayacam**",
"**hayır oflama**",
)

aynen = (
"**Aynen kardeşim**",
"**Aynen yaa**",
"**Ne aynen?**",
"**Biz kötüyüz aynen** ??",
"**Aynen tamam**",
"**Aynen bencede**",
)

ağla = (
"**Sen ağla**",
"**Niye ağlamıyorsun?***",
"**Ağlıyorum**",
"**Ağladın mı?**",
"**Ağlayacam'** ??",
"**Ağlattın**",
"**Sende ağla**",
"**Ağla kalbim ağlaa** ??",
"**Ağla iyi gelir**",
)

ağlama = (
"**Ağlama**",
"**Niye ağlıyorsun?**",
"**Ağlama artık**",
"**Ağlama tamam**",
"**Kim ağlattı seni?**",
"**Ağla kazanamadın**",
"**Bizde onları ağlatalım**",
)

yaren = (
"@the_alya_albora @The_cihan_albora onlar mükemmel aşklardı 💞",
"Mehmet deyince aklıma hep @the_alya_albora @The_cihan_albora geliyor ✨",
"Aşkın adı = @the_alya_albora & @The_cihan_albora 💕",
"Gerçek sevda dersen, işte @the_alya_albora @The_cihan_albora 🌹",
"Onlar efsane çift: @the_alya_albora @The_cihan_albora 💫",
"Mehmet benim canımdır ❤️",
"Her şeyim @the_alya_albora & @The_cihan_albora 💖",
"Onlar efsane aşklar ✨",
"Gerçek sevda = @the_alya_albora @The_cihan_albora 💞",
"Kalbim onların için atıyor 💘",
"Mehmet aşkın ta kendisi 💫",
"Onların sevgisi masal gibi 🌹",
"Kalbim sadece @the_alya_albora & @The_cihan_albora için atıyor ❤️",
"Onlar efsanevi bir çift 💕",
"Her zaman aklımda @the_alya_albora @The_cihan_albora ✨",
"@the_alya_albora @The_cihan_albora aşkları gibisi yok 💘",
"Yaren deyince direkt aklıma @the_alya_albora @The_cihan_albora geliyor 🌹",
"Onların sevgisi masal gibi: @the_alya_albora @The_cihan_albora 💞",
"Kalbin en güzel hali = @the_alya_albora @The_cihan_albora ✨",
"Onlar sonsuz aşkın adıydı: @the_alya_albora @The_cihan_albora 💫",
"Yaren bir tanedir 💖",
"Her zaman aklımda @the_alya_albora & @The_cihan_albora 💞",
"Onların aşkı efsane ✨",
"Kalbim sadece onlar için atıyor 💘",
"Sevda = @the_alya_albora @The_cihan_albora 🌹",
"Yaren canımın içi 💫",
"Onlar gerçek sevdanın adı 🌹",
"Her zaman aklımda @the_alya_albora & @The_cihan_albora ❤️",
"Aşkın tanımı = @the_alya_albora @The_cihan_albora 💕",
"Onlar efsanevi bir aşk 💞",
)

evet = ( 
"**Evet**",
"**Neye evet**",
"**Neden evet?**",
"**Evet, bencede**",
"**Evet mi?**",
"**Evet, olur**",
"**Evet, tamam**",
)

hmm = (
"**Hmm**",
"**Hımm**",
"**Sana hmm**",
"**Hmlama**",
"**Hm tamam**",
"**Hm neden?**",
"**Hmmmm**",
"**Hm, evet**",
)

hıhım = (
"**Hıhım**",
"**Hıhımm**",
"**Hıhım yapınca çok tatlı oluyorsun** ??",
"**Hıhım evet**",
"**Hıhım, tamamm**",
"**Hıhım ya**",
"**Hıhım olur**",
"**Sana da hıhım**",
)

git = (
"**Nereye?**",
"**Beni mi kovuyorsun???**",
"**Sen yürü git**",
"**Ne diyon lan**",
"**Gitmiyorum**",
"**Sen git**",
"**Kime yürü git diyorsun sen?**",
"**Bana mı dedin?**",
"**Tamam, gidiyorum.** ??",
)

komedi = (
"**Komedi mi?**",
"**Komediyen misin?**",
"**Komedi severim**",
"**Sevmem**",
"**Komedi mi seviyorsun?**",
"**Komedi seviyor musun**",
)

kanka = (
"**Kanka mı?**",
"**Efendim kanka?**",
"**Kankan mıyım?**",
"**Kankan değilim**",
"**Ne oldu kanka?**",
"**Niye kanka**",
"**Tamam kanka**",
"**Peki kankam**",
"**Kankamsın** ❤️",
"**Ne diyon kanka?**",
"**İyi misin kanka?**",
"**Naber kanka?**",
"**Ooo kanka**",
)

ban = (
"**Eline sağlık hak etmişti**",
"**Nedenini bilmesemde hak etmiştir**",
"**Neden yaptın bunu?**",
"**Bence Yapmamalısın**",
)

sen = (
"**Ben**",
"**Sen mi**",
"**Ben mi**",
"**Ne ben?**",
"**Ne sen?**",
"**Neden ben?**",
"**Neden sen?**",
"**Beni mi yapacam**",
"**Sen seviyor musun?**",
"**Sen yap**",
"**Nee sen mi?**",
"**Evet sen**",
"**Yok sen**",
)

hiç = (
"**Ne hiç?**",
"**Hiç mi?**",
"**Evet hiç**",
"**Bir hiç miyim**",
"**Ne demek hiç?**",
"**Hiç olmaz**",
"**Hiç mi yok?**",
"**Hiç yani**",
)

aç = (
"**Aç**",
"**Neyi açayım?**",
"**Telefonu aç**",
"**Gözünü aç**",
"**Kapı çalıyor kapıyı aç**",
"**Açtın mı?**",
"**Aç mı?**",
"**Niye?**",
"**Açmam**",
)

barışalım  = (
"**Barışalım mı?**",
"**Barıştık mı?**",
"**Barışmalıyız**",
"**Hadi barışalım**",
"**Öp elimi barışalım**",
"**Olur barışalım**",
"**Barıştık**",
"**Evet**", 
"**Olmaz**",
)

şimdi = (
"**Şimdi gel**",
"**Şimdi mi?**",
"**Ne şimdi?**",
"**Neden şimdi**",
"**Şimdi olmaz**",
"**Şimdi sus**",
"**Şimdi geldim**",
"**Şimdi gördüm**",
"**Şimdi mi geldin**",
"**Şimdi geldi**",
)

varoş  = (
"**Iyy pis varoş**",
"**Varoş musun sen**",
"**Ne varoş insansın**",
"**Uza varoş**",
"**Varoşa bak be**",
"**Varoş amk**",
"**Siktir git varoş**",
"**Konuşma varoş oç**",
"**Varoşlar konuşamaz**",
"**Varoşa benziyor**",
"**Ben mi varoşum?**",
"**Kime varoş diyorsun lan sen?**",
)

arkadaş = (
"**Sen kimsin arkadaş?**",
"**Kimin arkadaşısın?**",
"**Arkadaşım**",
"**Arkadaş olalım mı**",
"**Benim arkadaşım o**",
"**Hayır benim**",
"**Canım arkadaşım**",
"**Vay arkadaş**",
)

sus = (
"**Sen sus**",
"**Hayır sen sus**",
"**Sus**",
"**Suss**",
"**Sus lan**",
"**Ben niye susuyorum?**",
"**Sen susacaksın**",
"**Hayır sus lan**",
"**Evet ya sen sus**",
"**Sen karışma sus**",
)

üzüldüm = (
"**Niye?**",
"**Neye üzüldün?**",
"**Kim üzdü?**",
"**Üzülme yaa**",
"**Kıyamam, üzülme** ??",
"**Üzüldün mü?**",
"**Neden?**",
"**Üzüldün mü sen?**",
"**Üzme kendini??**",
"**Bende**"
"**Bende üzüldüm**",
)

kötü = (
"**Yaa, çok mu kötü?**",
"**Neden?**",
"**Kötü mü oldun?**",
"**İyi ol**",
"**Kötü mü?**",
"**Kötü müsün?**",
"**Bende kötüyüm**",
"**Çok kötü**",
"**Çok kötüsün**",
"**Sensin**",
)

akşamlar = (
"**Sana da iyi akşamlar**",
"**Size de**",
"**Sana da**",
"**Hoş geldin**",
"**Nasıl geçti günün?**",
"**İyi akşamlar canım**",
"**Yeni mi geldin?**",
"**Nerdesin sen ya gözümüz yollarda kaldı**",
)

commandList = [
    "zar",
    "dart",
    "basket",
    "basket",
    "futbol",
    "bowling",
    "slot",
    "para",
    "mani",
    "saka",
    "d",
    "c"
]