HELP_1 = """<b><u>Admin Komandaları:</b></u>

Sadəcə komandaların başında <b>ç</b> əlavə edin və ya onları kanal üçün istifadə etmək üçün komandaların əvvəlində <b>ç</b> istifadə edin.

/pause - Hazırda oxunan yayını dayandırın.

/resume - Dayandırılmış yayını davam etdirin.

/skip - Hazırda oxunan yayını keçirin və növbəti treki oxumağa başlayın.

/end və ya /stop - Qoşulan təkrarları silin və hazırda oxunan yayını dayandırın.

/player - İnteraktiv oynatıcı panelini əldə edin.

/queue - Qoşulmuş treklərin siyahısını göstərin.

"""

HELP_2 = """<b><u>Auth İstifadəçiləri:</b></u>

Auth istifadəçiləri, söhbət üçün admin hüquqlarına sahib olmadan bota admin hüquqlarını əldə edə bilərlər.

/auth [istifadəçi adı/istifadəçi_ID] - Botun auth siyahısına bir istifadəçi əlavə edin.
/unauth [istifadəçi adı/istifadəçi_ID] - Auth istifadəçilərini auth siyahısından çıxarın.
/authusers - Qrupun auth istifadəçilərinin siyahısını göstərin.
"""

HELP_3 = """<u><b>Broadcast Xüsusiyyəti:</b></u> [yalnızca sudo istifadəçilər üçün]

/broadcast [mesaj və ya mesaja yanıt] - Mesajınızı botun server qruplarına broadcast edin.

<u>Broadcast rejimləri:</u>
<b>-pin</b> - Broadcast edilmiş mesajınızı server qruplarında pinləyin.
<b>-pinloud</b> - Broadcast edilmiş mesajınızı server qruplarında pinləyin və üzvlərə bildiriş göndərin.
<b>-user</b> - Mesajınızı botunuzu işə salmış istifadəçilərə broadcast edin.
<b>-assistant</b> - Mesajınızı botun köməkçi hesabından broadcast edin.
<b>-nobot</b> - Botu mesajı broadcast etməyə məcbur etməyin.

<b>Nümunə:</b> <code>/broadcast -user -assistant -pin Salam.</code>
"""

HELP_4 = """<u><b>Çat Qara Siyahısı Xüsusiyyəti:</b></u> [yalnızca sudo istifadəçilər üçün]

Botumuzu qıymətli botumuzu istifadə etmədən əvvəl şübhəli çatlarla məhdudlaşdırın.

/blacklistchat [chat ID] - Botu bu çatdan istifadə etməkdən məhdudlaşdırın.
/whitelistchat [chat ID] - Qara siyahıya alınmış çatı ağ siyahıya alın.
/blacklistedchat - Qara siyahıya alınmış çatların siyahısını göstərir.
"""

HELP_5 = """<u><b>İstifadəçilərin Qadağan Edilməsi:</b></u> [yalnızca sudo istifadəçilər üçün]

Qara siyahıya alınmış istifadəçiləri nəzarətdən keçirin, beləliklə onlar bot komandalarını istifadə edə bilməzlər.

/block [istifadəçi adı və ya istifadəçi ID-si] - İstifadəçini botumuzdan qadağan edin.
/unblock [istifadəçi adı və ya istifadəçi ID-si] - Qadağan edilmiş istifadəçini açın.
/blockedusers - Qadağan edilmiş istifadəçilərin siyahısını göstərir.
"""

HELP_6 = """"\<u>\<b>Əmrlərin Siyahısı:</b></u>

Siz audio/video nümayişi kanalında oxuna bilər.

/cplay - Tələb olunan səslərə audio nümayişi başladır.
/cvplay - Tələb olunan video əsərlərinə video nümayişi başladır.
/cplayforce və ya /cvplayforce - Davam edən audio/video nümayişi dayandır və tələb olunan əsərlərin nümayişi başladır.

/channelplay [Söhbət istifadəçi adı və ya ID] və ya [deaktiv] - Kanalı qrupa qoşur və göndərilən əmrə əsasən əsərlərin nümayişi başlayır."
"""

HELP_7 = """<u><b>Qlobal Qadagalar Xüsusiyyəti:</b></u> [yalnızca sudo istifadəçilər üçün]

- `/gban` [istifadəçi adı və ya ID] - İstifadəçini bütün söhbətlərdə qadağan edir və onu botdan istifadə etməkdən məhrum edir.
- `/ungban` [istifadəçi adı və ya ID] - Qlobal olaraq qadağan edilmiş istifadəçinin qadağasını açır.
- `/gbannedusers` - Qlobal olaraq qadağan edilmiş istifadəçilərin siyahısını göstərir.
"""

HELP_8 = """<b><u>Dövrə Yayımla:</b></u>

<b>İndi yayımlanan axın aşağıdakı əmr ilə təkrarlanacaq:</b>

- `/loop [aktivləşdir/söndür]` - İndi yayımlanan axının təkrarlanmasını aktivləşdirir və ya söndürür.
- `/loop [1, 2, 3, ...]` - Göstərilən say qədər təkrarlanmağa icazə verir.
"""

HELP_9 = """<u><b>Bakım Rejimi:</b></u> [yalnızca sudo-lar üçün]

- `/logs` - Botun fəaliyyətlərinin qaydalarını əldə edin.

- `/logger [aktivləşdir/söndür]` - Bot, botda baş verən fəaliyyətləri qeydə alacaq.

- `/maintenance [aktivləşdir/söndür]` - Botunuzun bakım rejimini aktivləşdirin və ya söndürün.
"""

HELP_10 = """<b><u>Pinğ və Status:</b></u>

- `/start` - Musiqi botunu başladın.
- `/help` - Komandaların izahı ilə Yardım menyunu əldə edin.

- `/ping` - Botun ping və sistem statusunu göstərir.

- `/stats` - Botun ümumi statuslarını göstərir.
"""

HELP_11 = """<u><b>Play Komandaları:</b></u>

- `v` - Video play üçün dayandır.
- `force` - Force play üçün dayandır.

- `/play` və ya `/vplay` - Tələb olunan treki videonun yayına salır.

- `/playforce` və ya `/vplayforce` - İndi yayında olan sürəti dayandır və tələb olunan treki yayına salır.
"""

HELP_12 = """<b><u>Qarışıq Oynatma:</b></u>

- `/shuffle` - Oynatma siyahısını qarışdırır.
- `/queue` - Qarışıq oynatılan siyahını göstərir.
"""

HELP_13 = """<b><u>Streamə Zəfər:</b></u>

- `/seek [saniyə cinsində müddət]` - Streami verilən müddətə getirir.
- `/seekback [saniyə cinsində müddət]` - Streami geriyə getirir.
"""

HELP_14 = """<b><u>Mahnı yükləmə:</b></u>

- `/song [mahnı adı/yt URL]` - YouTube-dan hər hansı bir treki MP3 və ya MP4 formatında yükləyin.
"""

HELP_15 = """<b><u>Sürət Əmriləri</b></u>

- `/speed` və ya `/playback` - Qrupdakı səs təhrifat sürətini tənzimləmək üçün.
- `/cspeed` və ya `/cplayback` - Kanalda səs təhrifat sürətini tənzimləmək üçün.
"""

HELP_16 = """<b><u>Musiqi Sözləri Əmrləri</b></u>

`/lyrics [mahnı adı]` - Tələb olunan mahnının sözlərini axtar və nəticələri göndər.
"""
