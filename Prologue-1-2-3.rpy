# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("Bạn")
define hn = Character("Nghĩaa")
define ca = Character("Arii")
define df = Character("Poster")
define ld1 = Character("Lucas")
define ld = Character("Lukase")
define aa = Character("???")
define aa1 = Character("Cậu bé")
define aa2 = Character("Nữ nhân viên")
define aa3 = Character("") #Dùng sau
define rb = Character("Richhard")
define mc = Character("Nhânn")
define th = Character("Shine")
define aa4 = Character("Cô gái")

define blackout = Fade(0.25, 0.0, 0.75)

init:
    $ flash = Fade(.25, 0, .75, color="#fff")
image dftech_doc = "poster_doc.jpg"
image dftech_ngang = "poster_ngang.jpg"

#default flag
default book = False

# flag part 2
default notpen1 = False
default notpen2 = False
#flag part 3
default stalker1 = False
default stalker2 = False

#flag stat point set:
default humanpoint = 0
default timepoint = 0
default lukase_affection = 0
default TH_event = 0

#position

transform left:
    xalign 0.10 yalign 0.0
transform right:
    xalign 0.90 yalign 0.0
transform mcp:
    xpos 115 ypos 478

# The game starts here.

label start:
    #(Giới thiệu nghề nghiệp mc)
    scene keodeo_sang1
    show mcs at mcp
    "    "
    "Tổng biên tập từng nói với tôi: ‘Dù có 100 năm nữa, thì tờ báo vẫn sẽ chỉ là tờ báo thôi.’"
    "Có những thứ theo thời gian sẽ thay đổi liên tục đến chóng mặt, chẳng hạn như kĩ thuật công nghệ khi những ý tưởng tân tiến có thể lập tức thay thế cái cũ."
    "Cách đây 100 năm, thế giới mới biết đến điện thoại cảm ứng, bây giờ thì nó chỉ là một tấm card mỏng dính hoặc thường được tích hợp vào các thiết bị gia dụng quanh bạn."
    "Nhưng những tờ báo hay những quyển sách giấy, có bao nhiêu năm đi nữa thì vẫn y như vậy, từ những năm 1980 đến những năm 2000 hay 2103 như hiện tại." 
    "Hoạ chăng kĩ thuật in ấn và đóng cuốn trở nên tốt hơn, tiết kiệm sức người hơn." 
    "Vậy tại sao nó không thay đổi ư? Vì không cần thiết chứ sao." 
    "Đúng là không ai cần giữ một tờ báo qua hai đời người, vì nếu để lưu trữ đã có bản điện tử rồi." 
    "Thế nhưng đa số người còn thích cầm tờ báo hay cuốn sách trên tay là những người mê mẩn cái cảm giác được lật giở từng trang sách và mùi giấy mùi mực."
    "Vì vậy mà sách báo là một trong những thứ ít ỏi không bị kéo theo sự thay đổi bất tận của thời gian."
    "Tất nhiên nhờ thế mà công việc của tôi ít nhiều cũng không có sự khác biệt với các ghi chép của nhân loại mấy trăm năm về trước."
    "Nghề nhà báo nói dễ nghe thì là ghi chép và phổ cập cho mọi người những khía cạnh thú vị và phong phú của cuộc sống."
    "Nói khó nghe, thì là tọc mạch chuyện người khác rồi hô lên cho cả thiên hạ cùng biết." 
    "Dù có là vế nào, thì đây là một công việc phải có những người bất chấp thị phi hay thậm chí sự dè bỉu từ người ngoài để thực hiện."
    "Và tôi là một trong số những kẻ bất chấp đó."
    scene congvien_sang1

    "Tôi nhận thấy mình không phải kẻ thích dài dòng, nên tôi sẽ mở đầu câu chuyện bằng cách đơn giản nhất."
    "Hôm nay trời nắng đẹp, tôi và ông bạn thân lâu năm - Nguyễn Hữu Nghĩaa - vừa mới từ quán cà phê trở về."
    "Vì vẫn còn sớm và chẳng có chuyện gì gấp gáp nên cả hai quyết định tản bộ tại công viên Mega Lawn."
    "Tôi liếc qua gương mặt anh, không khỏi thở dài."
    mc "Ly cà phê anh gọi size XL đúng không?"
    "Nghĩaa ném cho tôi cái nhìn khó hiểu, chắc chắn là đang thắc mắc tôi lại lên cơn khùng điên gì."
    hn "Ừ?"
    mc "Thế sao trông anh như chưa uống giọt nào vậy?"
    hn "Vậy là chú không biết rồi, đối với dân designer bọn anh, một cốc thôi thì không xi nhê."
    hn "Nếu muốn thực sự tỉnh táo, phải nốc cả trăm cốc mới đủ đô, và còn thêm mấy chục lon nước tăng lực, rồi cả…"
    mc "Lại còn nước tăng lực?"
    mc "Anh tính biến đồ uống thành phương tiện gây án hả?!"
    hn "Câu này hay đó, lưu lại sau này làm tiêu đề báo về anh đi."
    mc "... Gì đấy?"
    hn "Chú biết khi nào chúng ta mới thực sự được nghỉ ngơi không?"
    hn "Khi ngưng thở đó."
    mc "Ha ha… Anh vui tính ghê!"
    hn "Cám ơn, cám ơn."
    mc "Anh chắc biết đấy là câu mỉa mai nhỉ?"
    hn "Tích cực là một đức tính…"
    "Không để anh nói hết, tôi bước nhanh lên trước."
    "Nghĩaa còn chẳng buồn chạy đuổi theo, vì anh biết đến cuối cùng thì tôi sẽ lại là người phải đứng đợi anh."
    "Đến khi anh đuổi kịp thì cả hai đều cùng nghe thấy giọng nói vô cùng quen thuộc."
    #cg gặp Choi Arii
    scene cg_02
    aa "Là… anh Nghĩaa với cậu nhà báo thật nè!"
    mc "Ô, chị!"
    "Cô gái này là Choi Arii, hàng xóm của Nghĩaa."
    ca "Chào em. Chào anh."
    hn "Ừ. Dạo này thế nào rồi? Dạ dày còn đau không?"
    ca "Dạ, từ khi có Picobot thì em đã ổn hơn nhiều rồi."
    "Quả thực Arii bây giờ trông tràn đầy sức sống hơn so với ngày đầu tiên tôi gặp cổ rất nhiều."
    scene room #thay bằng cảnh sau
    with fade
    "Hôm ấy cũng giống như hôm nay, tôi không hẹn mà sang nhà Nghĩaa để lôi anh ta ra khỏi nhà đi cà phê."
    #sound mở cửa
    mc "A, anh còn sống nè."
    "Tôi hớn hở chào hỏi ngay khi Nghĩaa mở cửa."
    hn "Có vẻ hôm nay chú rảnh rỗi quá nhỉ, còn nhớ tới thăm anh."
    "Nghĩaa không có vẻ ngạc nhiên lắm trước xuất hiện bất ngờ của tôi."
    hn "Anh đây bận lắm, có gì nói mau rồi phắn về giùm."
    "Vẫn giữ cái bản mặt u ám, một tay ảnh luồn vào sau áo gãi lưng, tay còn lại phẩy phẩy như muốn đuổi tôi đi thật nhanh."
    mc "Em đang rảnh thật, nay được nghỉ tính qua rủ anh làm chút cà phê."
    hn "Cà phê thì cũng cần đấy, nhưng phải ra ngoài thì…"
    mc "Anh đang bị deadline dí à?"
    mc "Không sao, anh mang luôn laptop theo đi ."
    mc "Em nói của em, anh làm của anh."
    mc "Nghe được đến đâu thì nghe."
    "Nghĩaa nhìn tôi với đôi mắt ẩn chứa sự thương hại."
    hn "Chú mày đúng là cô đơn tới tuyệt vọng thật đó."
    mc "... À haha…"
    mc "Mà thế nhé, em đợi anh."
    "Tuy trưng ra vẻ mặt không hài lòng, Nghĩaa vẫn trở vào trong nhà chuẩn bị."
    "Vài phút sau ảnh bước ra, quần áo không khác gì, chỉ đeo thêm một chiếc ba lô đựng laptop sau lưng."
    hn "Đi lẹ trước khi anh mày đổi ý."
    mc "Vẫn theo chủ nghĩa tối giản hả anh?"
    hn "Đi với chú thì cần gì ăn diện."
    "Vừa rời khỏi nhà Nghĩaa được vài bước thì bỗng có một dáng người lảo đảo va thẳng vào tôi."
    mc "Ối!" with hpunch   
    scene cg_01
    
    "Chưa kịp định hình chuyện gì đang xảy ra, tôi đã theo phản xạ đỡ lấy cô gái vừa va phải mình."
    "Trông mặt cô tái mét, trọng lượng đổ dồn hết lên người tôi."
    "Tôi dìu cô ngồi tựa vào bức tường sát hành lang."

    mc "Chị có sao không?"
    ca "A… Xin lỗi, xin lỗi, do tôi đau bụng quá nên thấy hơi choáng…"
    hn "Ô, Arii?"
    mc "Người quen anh hả?"
    hn "Ừ, hàng xóm. Mà quan trọng hơn, sao cô lại đau bụng?"
    hn "Sáng giờ có ăn phải đồ hỏng hay gì không?"
    ca "Không… Chưa ăn gì hết…"
    mc "Vậy thì… Chắc là đau dạ dày rồi."
    "Có lần chạy deadline cho bên tòa soạn mà không ăn ngủ đúng giờ, tôi cũng từng phải đi khám vì đau bụng tưởng chớt."
    "Nhưng may có Picobot bảo kê nên bác sĩ bảo dạ dày vẫn ổn."
    "Ông già tôi thì cằn nhằn vì bảo giới trẻ bây giờ chịu đau kém quá."
    "Tôi cá chắc ngày xưa ổng cũng bị ông nội tôi nhằn y chang."
    ca "Ừm… Hôm nay nhiều việc quá nên chưa–"
    "Chưa kịp dứt lời, Arii liền ngất đi."
    hn "Xem ra là kiệt sức rồi."
    "Để cơ thể đến mức này thì… có khi cô ấy không có tiêm Picobot."
    "Nên tình trạng còn nghiêm trọng hơn hồi tôi bị nữa."

    menu:

        "Tự mình bế Choi Arii":
            scene cg_01_1
            "Tôi lục túi áo, lấy ra một hộp cao sao đỏ rồi bôi lên thái dương với hy vọng Arii sẽ tỉnh lại."
            hn "Cái gì đấy?"
            mc "Thần dược."
            scene cg_01_2
            "Cái này hồi đó ông già nhà tôi nói là bôi dầu nóng thì giúp người ngất tỉnh được thì phải."
            "Mà trong túi tôi cũng có sẵn hộp cao."
            "Không có phản ứng."
            "Chắc là… áp dụng tùy người."
            hn "Thần dữ chưa bây?"
            mc "Phải đến bệnh viện rồi."
            "Tôi bế cô ấy lên trong khi Nghĩaa nhanh chóng gọi taxi."
            jump choice1_done

        "Để Nghĩaa bế Choi Arii":
            "Cẩn thận đỡ Arii cho Nghĩaa bế xong, tôi nhanh chóng gọi taxi để đưa cô ấy đến bệnh viện."
            jump choice1_done

    label choice1_done:
        #...

    scene benhvien #bệnh viện
    #with (transition)
    "Sau khi giúp Arii hoàn thành thủ tục, chúng tôi ngồi nghỉ tại băng ghế trống trong khuôn viên bệnh viện."

    hn "À, cổ bằng tuổi anh nên chú phải kêu bằng chị đấy."
    mc "Biết rồi mà."
    mc "Lần này chị ấy may đó! Tuy là loét dạ dày nhưng phát hiện kịp thời."
    hn "Ờ, ngất chỗ nào vắng người thì nguy."
    mc "Anh lo cho bản thân đi. Chạy deadline mà hom hem cả người."
    hn "Lo gì, anh mày tiêm Picobot rồi mà."
    hn "Mà chết rồi thì khỏi phải chạy deadline, càng sướng chứ sao."
    "Trình độ đùa nhạt của Nghĩaa vươn tới cấp địa ngục luôn rồi."
    "Picobot không phải toàn năng, nhưng nó đã thay đổi lối sống của nhân loại không ít."
    show dftech_doc
    #thêm ảnh poster dọc của DFTech
    df "Điện thế màng là tín hiệu điện thế giữa tế bào chất và không gian ngoại bào."
    df "Trường điện sinh học này giúp truyền thông tin giữa các tế bào với nhau, qua đó giúp các tế bào có thể giao tiếp với nhau."
    df " Giao tiếp giữa các tế bào giúp duy trì cân bằng nội mô, tìm ra những rối loạn và sửa chữa chúng."
    df "Picobot có khả năng tác động lên trường điện sinh học này giúp tăng cường hệ miễn dịch của cơ thể, nhờ đó loại trừ bệnh tật ngay từ khi chỉ còn là mầm mống."
    hide dftech_doc
    show dftech_ngang
    #thêm ảnh poster ngang của DFTech
    "Đó là phần quảng cáo sản phẩm mà DFTech đăng trên website của họ."
    "Tính ra khả năng marketing của công ty này cũng đỉnh lắm nha."
    "Để người khác tin tưởng vào một thứ gì đó họ không thể thấy, sờ…"
    "... hay cảm nhận được bằng bất cứ giác quan nào khác như con bot này thật sự không dễ dàng."
    "Ở một góc độ nào đó, khoa học và tôn giáo có khá nhiều điểm tương đồng."
    "Nhưng DFTech cũng đưa ra khuyến cáo rằng, vì Picobot hoạt động dựa trên hệ miễn dịch để tránh tình trạng quá mẫn…"
    "Nên người tiêm Picobot cũng phải có lối sống lành mạnh, sinh hoạt điều độ để phát huy tối đa khả năng của con bot."
    "Với lũ nô lệ tư bản cắm mặt vào deadline bỏ bê sức khỏe như tụi tôi, nếu con AI điều khiển Picobot có thể tự do suy nghĩ…"
    "Nó sẽ chửi tụi tôi sấp mặt."
    "Nhưng mà DFTech có cam kết AI họ dùng không được dạy dữ liệu khác ngoài y học hay sinh học để bảo vệ riêng tư cho người dùng…"
    "Nên tôi không nghĩ nó đủ khôn để biết chửi thề đâu."
    scene congvien_sang1
    #with flash
    "Trở lại hiện tại, Arii đang nói chuyện vui vẻ với Nghĩaa thì bỗng đưa mắt nhìn tôi."
    ca "Em cũng tới dự đúng không?"
    mc "Dạ, dự gì ạ?"
    hn "Nãy giờ hồn chú mày để ở tầng mây nào đó?"
    mc "Xin lỗi, em mải suy nghĩ vài thứ."
    hn "Haiz, chịu mày luôn."
    hn "Arii mời chú mày tới dự tiệc đính hôn của cổ và bạn gái, nhà hàng Grandelius."
    hn "Ngày 20 tháng này."
    "Ngày 20 tháng 2 sao… Hôm đó…"

    menu:
        "Cũng rảnh, đi thôi.":
            scene cg_02_agree
            "...cũng khá rảnh. Tuy còn hạn nộp bài cho bên tòa soạn vào 24…"
            "Nhưng chẳng sao hết, tôi tin mình có thể hoàn thành công việc đúng hạn."
            "Tôi gật đầu đồng ý với Arii ngay."
            mc "Chắc chắn em phải tới góp vui rồi!"
            "Hơn nữa nơi nào càng đông người, nơi đó tất có thị phi."
            "Mà một bữa tiệc thì sao?"
            "Đó chính là một trường săn tin tức đầy hấp dẫn."
            "Một nhà báo cao thủ không bằng tranh thủ như tôi thì làm sao bỏ qua được."
            jump choice2_party

        "Còn cái deadline ngày 24 này phải nộp.":
            scene cg_02_decline
            mc "Chắc… em không thể tham dự rồi."
            mc "Tại em vừa nhớ ra mình còn cái deadline vào 24… Nếu đi dự tiệc thì sợ không kịp mất."
            mc "Nhưng dù sao thì cảm ơn chị đã mời nhé!"
            "Nét mặt Arii tràn đầy tiếc nuối."
            ca "Đành vậy, công việc cũng rất quan trọng mà ha!"
            "Nghĩaa đứng bên thì lại huých khuỷu tay tôi mấy cái."
            hn "Tuy chú không đi nhưng nhớ gửi tiền mừng cho em nó đấy."
            mc "Dĩ nhiên! Chứ không thì sau này tới đám cưới em thì chị ấy sẽ không thèm tới dự mất!"
            jump choice2_done

    label choice2_done:
        #Lựa chọn không đến bữa tiệc
        return #debug, khi xong bỏ


    label choice2_party:
        scene nhahang
        "Ngày 20 tháng 2 năm 2101, tại nhà hàng Grandelius."
        "Khu tiệc ngoài trời tấp nập người qua lại, âm thanh trò chuyện rì rầm vang lên từ mọi hướng."
        mc "Chúc mừng chị Arii, phải hạnh phúc đó."
        ca "Cảm ơn cậu!"
        "Chị gật đầu, mỉm cười với chúng tôi, rồi cùng người yêu đi chào hỏi những người khác."
        "Xung quanh, mỗi người đều đang bận rộn với công việc và câu chuyện của riêng họ."
        "Có nam nhân viên đang loay hoay tìm gì đó dưới sàn, nữ nhân viên lóng ngóng với khay thức uống trên tay, cậu bé đùa nghịch với chiếc khăn trải bàn, và anh trai bên cạnh tôi đây."
        menu:
            "Bắt chuyện với nam nhân viên":
                jump waiter
            "Bắt chuyện với nữ nhân viên":
                jump waitress
            "Bắt chuyện với Nghĩaa":
                jump friend
            "Bắt chuyện với cậu bé":
                jump kid

        label waiter:
            #Nam nhân viên
            "Tôi quyết định đến xem thử nam nhân viên nọ."
            mc "Xin chào?"
            #để sprite Lukase
            aa "A? Xin chào… Ừm… Xin lỗi, quý khách có thấy cái bảng tên nào gần đây không?"
            "Vậy ra anh ta đang tìm bảng tên."
            mc "Không có. Mà ông tên gì ấy? Để tôi tìm giúp cho."
            "Anh ta có vẻ chần chừ."
            ld1 "Thật ngại quá… Tôi tên {i}Lucas{/i}."
            mc "Ok, tôi tìm thử xem. Khi nào thấy thì sẽ đưa ông."
            ld1 "Vậy cảm ơn… rất nhiều!"
            "Tôi bắt đầu tìm kiếm xung quanh, lẩm nhẩm cái tên ‘{i}Lucas{/i}’ trong đầu."
            "Không tìm thấy."
            "Bên này cũng không có."
            "Chợt, giọng nói của nam nhân viên khi nãy vang lên."
            ld1 "A! Tôi thấy nó rồi!"
            "Vừa ngẩng đầu lên gật với anh ta hai cái, thì một âm thanh khác đã thu hút sự chú ý của tôi."
            menu:
                "Tiếng kêu":
                    hn "Nhânn! Đang làm gì đó? Lại đây cái đi."
                    "Là Nghĩaa."
                    "Tôi nhanh chóng bước đến cạnh anh ta."
                    hn "Lát anh tính chuồn về sớm còn chạy deadline. Chú mày đi không?"
                    mc "Anh cứ đi đi. Có gì em báo Arii cho."
                    hn "Nói thôi, đừng có mà báo."
                    mc "... Bánh đậu phộng ở đây ngon ha anh."
                    "Trong lúc đưa mắt nhìn xung quanh để tìm chủ đề cho cuộc trò chuyện nhạt nhẽo (như mọi khi), tôi chợt thấy một người phục vụ đứng gần đó nhợt nhạt bất thường, trên mặt mồ hôi đầm đìa."
                    "Đó là… Lucas?"
                    jump choice3_ld
                "Tiếng hét":
                    aa1 "AAAAA!"
                    "Tiếng hét đến từ một cậu bé tầm năm tuổi đang cầm chặt tấm khăn trải bàn trong tay."
                    "Bên cạnh là nữ nhân viên trông rất lo lắng và luống cuống."
                    aa2 "Bé ơi, đừng nghịch nữa mà! Đồ ăn rơi hết mất!"
                    aa1 "Không! Không không không!"
                    "Hết cách, tôi đành tiến lại chỗ họ."
                    mc "Nhóc, ăn kẹo không? Lại đây."
                    "Trò cũ rích. Ấy vậy mà thằng bé buông tay thật."
                    "Đôi chân ngắn ngủn lạch bạch chạy về phía tôi, lòng bàn tay giơ ra chờ đợi."
                    "Cũng may trong túi vẫn còn mấy viên kẹo cà phê - phòng trường hợp Nghĩaa ngáp ngắn ngáp dài ngay giữa bữa tiệc."
                    "Tôi nhét vào bàn tay thằng bé ít kẹo, rồi túm lấy cánh tay nó."
                    mc "Đi, đi tìm người nhà của nhóc. Ngoan thì tí anh cho thêm kẹo."
                    "Lúc này thằng bé có vẻ nghe lời hẳn."
                    "Đưa nó về cho gia đình xong, tôi chợt thấy một người phục vụ đứng gần đó nhợt nhạt bất thường, trên mặt mồ hôi đầm đìa."
                    "Đó là… Lucas?"
                    jump choice3_ld
        label waitress:
            "Tôi quyết định đến xem thử nữ nhân viên."
            "Bên cạnh cô là một cậu bé tầm năm tuổi đang cầm chặt tấm khăn trải bàn."
            show nvn 
            aa2 "Bé ơi, đừng nghịch nữa mà! Đồ ăn rơi hết mất!"
            aa1 "Không! Không không không!"
            "Hết cách, tôi đành lên tiếng."
            mc "Nhóc, ăn kẹo không? Lại đây."
            "Trò cũ rích."
            "Ấy vậy mà thằng bé buông tay thật."
            "Đôi chân ngắn ngủn lạch bạch chạy về phía tôi, lòng bàn tay giơ ra chờ đợi."
            "Cũng may trong túi vẫn còn mấy viên kẹo cà phê - phòng trường hợp Nghĩaa ngáp ngắn ngáp dài ngay giữa bữa tiệc."
            "Tôi nhét vào bàn tay thằng bé ít kẹo, rồi túm lấy cánh tay nó."
            mc "Đi, đi tìm người nhà của nhóc. Ngoan thì tí anh cho thêm kẹo."
            "Lúc này thằng bé có vẻ nghe lời hẳn."
            "Đưa nó về cho gia đình xong…"
            menu:
                "Đến chỗ nam nhân viên":
                    "Tôi quyết định đến xem thử nam nhân viên đang loay hoay tìm gì đó dưới sàn."
                    mc "Xin chào?"
                    # Đổi sprite Lukase
                    "A? Xin chào… Ừm… Xin lỗi, quý khách có thấy cái bảng tên nào gần đây không?"
                    "Vậy ra anh ta đang tìm bảng tên."
                    mc "Không có. Mà ông tên gì ấy? Để tôi tìm giúp cho."
                    "Anh ta có vẻ chần chừ."
                    ld1 "Thật ngại quá… Tôi tên {i}Lucas{/i}."
                    mc "Ok, tôi tìm thử xem. Khi nào thấy thì sẽ đưa ông."
                    ld1 "Vậy cảm ơn… rất nhiều!"
                    "Tôi bắt đầu tìm kiếm xung quanh, lẩm nhẩm cái tên ‘{i}Lucas{/i}’ trong đầu."
                    "Không tìm thấy."
                    "Bên này cũng không có."
                    "Chợt, giọng nói của nam nhân viên khi nãy vang lên."
                    ld1 "A! Tôi thấy nó rồi!"
                    "Vừa ngẩng lên gật đầu hai cái thì tôi đã nhận ra có gì đó không ổn."
                    jump choice3_ld
                "Đến chỗ Nghĩaa":
                    #[+1 điểm Human.]
                    $ humanpoint += 1
                    hn "Nhânn! Đang làm gì đó? Lại đây cái đi."
                    "Là Nghĩaa."
                    "Tôi nhanh chóng bước đến cạnh anh ta."
                    hn "Lát anh tính chuồn về sớm còn chạy deadline. Chú mày đi không?"
                    mc "Anh cứ đi đi. Có gì em báo Arii cho."
                    hn "Nói thôi, đừng có mà báo."
                    mc "... Bánh đậu phộng ở đây ngon ha anh."
                    "Và tôi đã nghe (chịu đựng) những trò đùa tẻ nhạt của Nghĩaa đến khi anh ta rời đi."
                    "Bữa tiệc diễn ra khá yên bình cho đến khi gần kết thúc."
                    jump choice3_done
        label friend:
            "Trong lúc mải nghĩ ngợi, tôi nghe thấy người bên cạnh lên tiếng."
            hn "Lát anh tính chuồn về sớm còn chạy deadline. Chú mày đi không?"
            mc "Anh cứ đi đi. Có gì em báo Arii cho."
            hn "Nói thôi, đừng có mà báo."
            mc "... Bánh đậu phộng ở đây ngon ha anh."
            "Trong lúc ngó nghiêng tìm chủ đề cho cuộc trò chuyện nhạt nhẽo (như mọi khi), tôi chợt thấy hai người phục vụ trông có vẻ bất ổn."
            menu:
                "Bắt chuyện với nam nhân viên":
                    "Tôi quyết định đến xem thử nam nhân viên đang loay hoay tìm gì đó dưới sàn."
                    mc "Xin chào?"
                    # đổi sprite Lukase
                    "A? Xin chào… Ừm… Xin lỗi, quý khách có thấy cái bảng tên nào gần đây không?"
                    "Vậy ra anh ta đang tìm bảng tên."
                    mc "Không có. Mà ông tên gì ấy? Để tôi tìm giúp cho."
                    "Anh ta có vẻ chần chừ."
                    ld1 "Thật ngại quá… Tôi tên {i}Lucas{/i}."
                    mc "Ok, tôi tìm thử xem. Khi nào thấy thì sẽ đưa ông."
                    ld1 "Vậy cảm ơn… rất nhiều!"
                    "Tôi bắt đầu tìm kiếm xung quanh, lẩm nhẩm cái tên ‘{i}Lucas{/i}’ trong đầu."
                    "Không tìm thấy."
                    "Bên này cũng không có."
                    "Chợt, giọng nói của nam nhân viên khi nãy vang lên."
                    ld1 "A! Tôi thấy nó rồi!"
                    "Vừa ngẩng đầu lên gật với anh ta hai cái, thì một âm thanh khác đã thu hút sự chú ý của tôi."
                    jump choice3_ld
                "Bắt chuyện với nữ nhân viên":
                    $ humanpoint += 1
                    #[+1 điểm Human.]
                    "Tôi quyết định đến xem thử nữ nhân viên lóng ngóng với khay thức uống trên tay."
                    "Bên cạnh cô là một cậu bé tầm năm tuổi đang cầm chặt tấm khăn trải bàn."
                    aa2 "Bé ơi, đừng nghịch nữa mà! Đồ ăn rơi hết mất!"
                    aa1 "Không! Không không không!"
                    "Hết cách, tôi đành tiến lại chỗ họ."
                    mc "Nhóc, ăn kẹo không? Lại đây."
                    "Trò cũ rích."
                    "Ấy vậy mà thằng bé buông tay thật."
                    "Đôi chân ngắn ngủn lạch bạch chạy về phía tôi, lòng bàn tay giơ ra chờ đợi."
                    "Cũng may trong túi vẫn còn mấy viên kẹo cà phê - phòng trường hợp Nghĩaa ngáp ngắn ngáp dài ngay giữa bữa tiệc."
                    "Tôi nhét vào bàn tay thằng bé ít kẹo, rồi túm lấy cánh tay nó."
                    mc "Đi, đi tìm người nhà của nhóc. Ngoan thì tí anh cho thêm kẹo."
                    "Lúc này thằng bé có vẻ nghe lời hẳn."
                    "Đưa nó về cho gia đình xong, tôi quay lại tận hưởng bữa tiệc đến khi gần kết thúc."
                    jump choice3_done
        label kid:
            "Tôi quyết định đến xem cậu bé đằng xa, chỗ chiếc khăn trải bàn bày đống ly tách dễ vỡ trên đấy."
            "Chiếc bàn đã có chút lung lay trước sự tác động của thằng bé."
            "Hoảng hốt, tôi vội chạy tới, chụp lấy nó rồi cố nhấc ra khỏi đó."
            "Thế nhưng lực tay lẫn sự ngoan cố của đứa nhóc này đều rất lớn."
            "Thay vì tách nó ra khỏi tấm khăn, tôi đã vô tình giúp thằng nhóc giật chiếc khăn trải bàn, khiến những thứ trên đấy nghiêng ngả rồi văng tứ tung."
            "Những chiếc ly rơi xuống đất khiến mảnh vỡ văng tung tóe."
            "Có mảnh bắn vào cổ họng tôi, đau điếng người."
            "Duy chỉ có tấm khăn trải bàn là vẫn vẹn nguyên trong tay thằng bé."
            "Đúng là top 1 những thứ vừa nhanh vừa chắc chắn nhất trên thế giới, đối lập với những lời hứa hẹn yêu đương của người yêu cũ."
            "Mọi người nháo nhào cả lên, người tụ vào, người tản ra, hòng dọn dẹp hoặc né tránh sự cố."
            "Nhưng tôi không thể biết chuyện gì xảy ra sau đó nữa."
            "Vết thương ở cổ ngày càng đau."
            "Tầm mắt tôi mờ dần, mờ dần đi, cho đến khi hoàn toàn chẳng còn thấy chút ánh sáng nào."
            scene bg room #bg đen xì
            with fade
            jump badend #variation?
            "“Bài học rút ra là: Đừng có lo chuyện bao đồng dính dáng tới tụi con nít quỷ.”"

        label choice3_ld:
            "Tôi chạy về phía Lucas."
            "Trông sắc mặt anh ta vô cùng nhợt nhạt, mồ hôi đầm đìa từ trán đến cổ."
            mc "Này, ông ổn không đó?"
            ld1 "Không… Tôi nghĩ mình cần… ngồi xuống đã."
            "Tôi gật đầu, nhanh tay kéo chiếc ghế gần đó lại rồi dìu Lucas ngồi xuống."
            "Hơi thở ngày càng nặng nề."
            "Khuôn mặt dần sưng phù lên."
            "Làn da trở nên đỏ ửng."
            menu:
                "Anh bị hen suyễn à?":
                    jump x1
                "Anh bị con gì cắn phải à?":
                    jump x2
                "Anh có bị dị ứng với thứ gì không?":
                    jump v

        label x1:
            #Hen suyễn
            "Trông anh ta có vẻ khó thở, nói không chừng là cơn hen tái phát."
            ld1 "Không… Tôi bị… dị ứng."
            mc "Ông cần tôi giúp gì không?"
            ld1 "Epi… Pen…"
            "Và rồi anh ta ngất đi."
            "Chờ đã, EpiPen là sao chứ?"
            $ timepoint += 1
            #[+1 Thời gian.]
            jump epipen
        label x2:
            #Bọ
            "Trông anh ta có vẻ khó thở, nói không chừng là cơn hen tái phát."
            ld2 "Không… Tôi bị… dị ứng."
            mc "Ông cần tôi giúp gì không?"
            ld1 "Epi… Pen…"
            "Và rồi anh ta ngất đi."
            "Chờ đã, EpiPen là sao chứ?"
            $ timepoint += 1
            #[+1 Thời gian.]
            jump epipen
        label v:
            #Lựa chọn đúng, dị ứng
            "Các biểu hiện của anh ta rất giống sốc phản vệ - loại phản ứng dị ứng nghiêm trọng tôi từng đọc trên mạng."
            ld1 "Đậu phộng… Epi… Pen…"
            "Và rồi anh ta ngất đi."
            "Chờ đã, EpiPen là sao chứ?"
            jump epipen
        label epipen:
            menu:
                "Thiết bị máy liên lạc với Picobot?":
                    jump comm
                "Lucas muốn xin chữ ký?":
                    jump autograph
                "Thuốc tiêm ngừa dị ứng?":
                    jump pen

        label comm:
            #Thiết bị liên lạc
            mc "Hả? Nhưng Picobot tự kích hoạt được mà?"
            "Tôi cá chắc anh chàng này dùng đồ lậu hoặc hàng kém chất lượng."
            "Làm gì mà cần điều khiển Picobot chứ?"
            $ timepoint += 1
            #[+1 Thời gian.]
            "Lúc này, bỗng nhiên cô nhân viên lúc nãy chạy đến."
            aa2 "Ối trời, {i}Lucas{/i}! Đã bảo anh cẩn thận rồi!"
            "Cô ấy có vẻ quen Lucas và biết được điều gì đó."
            mc "Trước khi ngất đi anh ta còn thều thào kêu EpiPen, hình như là muốn liên lạc với Picobot."
            "Vừa dứt lời, tôi đã bị nhìn bằng ánh mắt kì lạ."
            aa2 "EpiPen là bút tiêm epinephrine dành cho người có nguy cơ hoặc tiền sử dị ứng, để họ tự dùng thuốc trong trường hợp khẩn cấp đó."
            "Thì ra là vậy."
            mc "Bình thường Lucas hay để nó ở đâu?"
            aa2 "Trong phòng nhân viên, để tôi dẫn anh đến đó."
            mc "Được."
            jump staffroom1
        label autograph:
            #chữ kí
            "EpiPen… là bút nhỉ? Vậy là Lucas muốn xin chứ ký sao?"
            "Anh ta thích tôi nhanh vậy à? Hay là từng đọc báo tôi viết?"
            "Thôi được rồi."
            "Tôi lấy ra cuốn sổ tay cùng với bút bi - hai vật bất ly thân của người trong ngành - và ký tên."
            "Xong xuôi, tôi nhét tờ giấy chứa chữ ký vào túi áo Lucas."
            $ timepoint += 2
            #[+2 Thời gian.]
            "Lúc này, bỗng nhiên cô nhân viên lúc nãy chạy đến."
            aa2 "Ối trời, {i}Lucas{/i}! Đã bảo anh cẩn thận rồi!"
            "Cô ấy có vẻ quen Lucas và biết được điều gì đó."
            mc "Trước khi ngất đi anh ta còn thều thào kêu EpiPen, hình như là muốn xin chữ ký."
            "Vừa dứt lời, tôi đã bị nhìn bằng ánh mắt kì thị."
            aa2 "EpiPen là bút tiêm epinephrine dành cho người có nguy cơ hoặc tiền sử dị ứng, để họ tự dùng thuốc trong trường hợp khẩn cấp."
            "Thì ra là vậy."
            mc "Bình thường Lucas hay để nó ở đâu?"
            aa2 "Trong phòng nhân viên, để tôi dẫn anh đến đó."
            mc "Được."
            jump staffroom1
        label pen:
            #Lựa chọn đúng, EpiPen
            "Tôi nhớ ra rồi!"
            "EpiPen là bút tiêm epinephrine dành cho người có nguy cơ hoặc tiền sử dị ứng, để họ tự dùng thuốc trong trường hợp khẩn cấp."
            "Hồi viết một bài báo quảng cáo cho công ty thiết bị y tế tôi có từng đọc qua."
            #[+1 điểm thiện cảm Lukase.]
            #Kei: thêm sau
            "Vậy thì hẳn là nó sẽ ở đâu đó trên người anh ta."
            "Nghĩ vậy, tôi bèn thử lục lọi…"
            menu:
                "Túi quần trái":
                    "Không có gì trong đó cả."
                    mc "Hay là ở tủ đồ cá nhân?"
                    "Lúc này, bỗng nhiên cô nhân viên lúc nãy chạy đến."
                    aa2 "Ối trời, {i}Lucas{/i}! Đã bảo anh cẩn thận rồi!"
                    "Cô ấy có vẻ quen Lucas và biết được điều gì đó."
                    mc "Hình như anh ta bị dị ứng, trước khi ngất đi còn thều thào kêu EpiPen. Cô biết nó ở đâu không?"
                    aa2 "EpiPen, EpiPen ở phòng nhân viên! Để tôi dẫn anh đến đó."
                    mc "Được."
                    jump staffroom1
                "Túi quần phải":
                    "Bên trong có chiếc ví tiền chứa một tấm thẻ công dân."
                    "‘Lukase Dương’, một cái tên kì lạ."
                    "Song đây không phải chuyện quan trọng."
                    jump staffroom2
                "Túi áo trên ngực":
                    "Bên trong không có gì ngoài một chiếc bảng tên."
                    "‘Lukase’, một cái tên kì lạ."
                    "Song đây không phải chuyện quan trọng."
                    jump staffroom2

        label staffroom1:
                    scene nhahang2_sang1
                    "Trên đường đến phòng nhân viên, bỗng nhiên ánh sáng xung quanh biến mất."
                    
                    scene nhahang2_toi1 with blackout
                    show nvn
                    show mcs at mcp
                    "Tôi liền bật đèn pin điện thoại lên để chiếu sáng, cẩn thận bước theo cô ấy."
                    "Tình cờ nhìn lướt qua thời gian hiển thị trên đó."
                    "Tại sao xe cứu thương vẫn chưa đến nhỉ?"
                    "Nữ nhân viên cúi đầu nhìn điện thoại một thoáng, rồi ngẩng lên nói với tôi."
                    aa2 "Xin lỗi anh… Gần đây vừa có một vụ cháy nên phải ngắt điện tạm thời trong khu vực."
                    aa2 "Có vẻ như giao thông cũng bị ảnh hưởng…"
                    "Tôi gật đầu ra vẻ đã hiểu."
                    "Trên đường đi, cô kể về một số chuyện của Lucas."
                    aa2 "Lucas có hơi ít nói với hậu đậu, nhưng cũng hiền lành tốt bụng lắm."
                    aa2 "Ảnh còn dễ tin người cực, đặc biệt là người có ơn với mình."
                    aa2 "Hồi Lucas mới vào làm, còn chậm chạp chưa quen, có mấy hôm tôi phải giúp dọn dẹp đến tận khuya."
                    aa2 "Kể ra thì, bị dị ứng đến thế này, anh ta cũng bất cẩn quá…"
                    scene nhahang2_toi2 with dissolve
                    show nvn
                    show mcs at mcp        
                    "Nói đến đây, chúng tôi đã tới phòng nhân viên."
                    "Cô ấy mở cửa ra, đèn chợt sáng lên."
                    scene nhahang2_sang2 with flash
                    show mcs at mcp
                    show nvn
                    "Cùng lúc đó, có tiếng chuông điện thoại phát ra."
                    aa2 "A, tôi xin lỗi."
                    aa2 "Alo?... Vâng, tôi đến ngay."
                    "Đoạn, cô cúp máy, quay sang nói với tôi."
                    aa2 "Vụ cháy vừa được xử lý xong nên điện đã có lại, nhưng đang có nhiều khách hoang mang, muốn gọi người thân và rời đi, nên tình hình ngoài đó hơi lộn xộn…"
                    mc "Cô cứ đi đi, đang thiếu người mà nhỉ. Lấy thuốc xong tôi sẽ về ngay."
                    aa2 "Vâng, cảm ơn anh. Vậy tôi xin phép đi trước."
                    "Tôi gật đầu, nhìn cô ấy rời đi rồi mới quay sang xem xét dãy tủ đồ."
                    "Trong số mười chiếc tủ, không có cái tên ‘Lucas’ nào cả."
                    "Chỉ có ba cái tên gần giống nhất - Lucanus, Lukase, và Luke."
                    menu:
                        "Mở tủ 'Lucanus'" if not notpen1:
                            $ notpen1 = True
                            "Bên trong chỉ có chút đồ dùng bình thường."
                            "Không tìm thấy EpiPen."
                            $ timepoint += 2
                            #[+2 Thời gian.]
                        "Mở tủ 'Luke'" if not notpen2:
                            $ notpen2 = True
                            "Bên trong chỉ có chút đồ dùng bình thường."
                            "Không tìm thấy EpiPen."
                            $ timepoint += 2
                            #[+2 Thời gian.]
                        "Mở tủ 'Lukase'":
                            "Bên trong có chút đồ dùng bình thường, và cả EpiPen nằm trong túi hông của balo."
                            "Lukase?"
                            "Không phải cậu ta tên Lucas sao?"
                            "Mà rõ ràng đây cũng không có tủ đồ nào đề tên ‘Lucas’."
                            "..."
                            "Chờ đã."
                            "Nếu bỏ qua khả năng bị lừa hoặc cô nhân viên kia nhầm lẫn, thì đúng là anh chàng chưa từng đánh vần cái tên ‘L-u-c-a-s’."
                            "Chỉ có tôi tự mặc định là vậy."
                            "Ah, Starbuckz."
                            "Cách viết đúng phải là ‘L-u-k-a-s-e’."
                            "Hóa ra cái tên Lukase của anh ta khi đọc lên sẽ không có âm ‘e’ và giống ‘Lucas’."
                            "Thảo nào."
                            "Không dám nghĩ ngợi thêm nữa, tôi cầm theo EpiPen, vội vàng quay lại sảnh."
                            $ timepoint += 1
                            #[+1 Thời gian.]
                            # jump sau tính điểm thời gian

                        "Quay lại phòng tiệc hỏi":
                            scene nhahang2_sang1
                            "Không nên táy máy lung tung thì hơn."
                            "Tôi nghĩ mình nên quay lại hỏi rõ hơn cô nhân viên nọ."
                            "Khi vừa quay lại phòng tiệc, tôi đã thấy cảnh sát và nhân viên y tế xung quanh."
                            aa2 "Anh đây rồi. Ảnh vừa tắt thở... Chúng tôi đang cố gắng cứu vãn..."
                            "Lúc này tôi mới nhận ra, người nằm trên chiếc cán, giữa vòng vây của đám đông chính là Lucas."
                            $ humanpoint += 1
                            #[+1 điểm Human.]
                            jump badend

        label staffroom2:
                    "Lúc này, Nghĩaa chợt lên tiếng."
                    hn "EpiPen thì có khi nào để trong tủ đồ cá nhân không?"
                    "Lúc này, bỗng nhiên cô nhân viên lúc nãy chạy đến."
                    show nvn
                    aa2 "Ối trời, {i}Lucas{/i}! Đã bảo anh cẩn thận rồi!"
                    "Cô ấy có vẻ quen Lucas và biết được điều gì đó."
                    mc "Hình như anh ta bị dị ứng, trước khi ngất đi còn thều thào kêu EpiPen. Cô biết nó ở đâu không?"
                    aa2 "EpiPen, EpiPen ở phòng nhân viên! Để tôi dẫn anh đến đó."
                    mc "Được."
                    scene nhahang2_sang1 
                    show mcs at mcp
                    show nvn
                    "Tôi đi theo cô ấy đến một hành lang sang trọng nối giữa hai khu vực."
                    "Trên đường đến phòng nhân viên, bỗng nhiên ánh sáng xung quanh biến mất."
                    scene nhahang2_toi1 
                    with blackout
                    show mcs at mcp
                    show nvn
                    
                    
                    "Tôi liền bật đèn pin điện thoại lên để chiếu sáng, cẩn thận bước theo cô ấy."
                    "Tình cờ nhìn lướt qua thời gian hiển thị trên đó."
                    "Tại sao xe cứu thương vẫn chưa đến nhỉ?"
                    "Nữ nhân viên cúi đầu nhìn điện thoại một thoáng, rồi ngẩng lên nói với tôi."
                    aa2 "Xin lỗi anh… Gần đây vừa có một vụ cháy nên phải ngắt điện tạm thời trong toàn khu vực."
                    aa2 "Có vẻ như giao thông cũng bị ảnh hưởng."
                    "Tôi gật đầu ra vẻ đã hiểu."
                    "Trên đường đi, cô kể về một số chuyện của Lucas."
                    aa2 "Lucas có hơi ít nói với hậu đậu, nhưng cũng hiền lành tốt bụng lắm."
                    aa2 "Ảnh còn dễ tin người cực, đặc biệt là người có ơn với mình."
                    aa2 "Hồi Lucas mới vào làm, còn chậm chạp chưa quen, có mấy hôm tôi phải giúp dọn dẹp đến tận khuya."
                    aa2 "Kể ra thì, bị dị ứng đến thế này, anh ta cũng bất cẩn quá…"
                    scene nhahang2_toi2 with dissolve
                    show mcs at mcp
                    show nvn
                    "Nói đến đây, chúng tôi đã tới phòng nhân viên."
                    "Cô ấy mở cửa ra, đèn chợt sáng lên."
                    scene nhahang2_sang2 with flash
                    show mcs at mcp
                    show nvn
                    "Cùng lúc đó, có tiếng chuông điện thoại phát ra."
                    aa2 "A, tôi xin lỗi."
                    aa2 "Alo?... Vâng, tôi đến ngay."
                    "Đoạn, cô cúp máy, quay sang nói với tôi."
                    aa2 "Vụ cháy vừa được xử lý xong nên điện đã có lại, nhưng đang có nhiều khách hoang mang, muốn gọi người thân và rời đi, nên tình hình ngoài đó hơi lộn xộn…"
                    mc "Cô cứ đi đi, đang thiếu người mà nhỉ. Lấy thuốc xong tôi sẽ về ngay."
                    aa2 "Vâng, cảm ơn anh. Vậy tôi xin phép đi trước."
                    "Tôi gật đầu, nhìn cô ấy rời đi rồi mới quay sang xem xét dãy tủ đồ."
                    "Trong số mười chiếc tủ, không có cái tên ‘Lucas’ nào cả."
                    "Chỉ có ba cái tên gần giống nhất - Lucanus, Lukase, và Luke."
                    menu:
                        "Mở tủ 'Lucanus'":
                            "Vừa mở tủ ra, nữ nhân viên lại chạy đến."
                            aa2 "Hộc… Lucas… Ảnh tắt thở rồi… Chúng tôi đang cố gắng cứu vãn."
                            "Chết tiệt…"
                            "Tôi vội theo nhân viên nữ quay trở lại sảnh."
                            "Ra đến nơi, tôi chỉ kịp nhìn thấy Lukase được đưa đi trên cán cứu thương."
                            $ humanpoint += 1
                            #[+1 điểm Human.]
                            jump badend
                        "Mở tủ 'Luke'":
                            "Vừa mở tủ ra, nữ nhân viên lại chạy đến."
                            aa2 "Hộc… Lucas… Ảnh tắt thở rồi… Chúng tôi đang cố gắng cứu vãn."
                            "Chết tiệt…"
                            "Tôi vội theo nhân viên nữ quay trở lại sảnh."
                            "Ra đến nơi, tôi chỉ kịp nhìn thấy Lukase được đưa đi trên cán cứu thương."
                            $ humanpoint += 1
                            #[+1 điểm Human.]
                            jump badend
                        "Mở tủ 'Lukase'":
                            "Lukase?"
                            "Bên trong có chút đồ dùng bình thường, và cả EpiPen nằm trong túi hông của balo."
                            "Phải rồi, là cái tên ban nãy."
                            "Không dám nghĩ ngợi thêm nữa, tôi cầm theo EpiPen, vội vàng quay lại sảnh."
                            #jump sau tính điểm thời gian
                            if timepoint >= 4:
                                jump overtime
                            if timepoint <= 3:
                                jump ontime

        # cơ chế tính điểm thời gian?
        label overtime:
            #nhiều hơn 4 điểm thời gian
            scene nhahang
            "Ra đến nơi, tôi chỉ kịp nhìn thấy Lukase được đưa đi trên cán cứu thương."
            aa2 "Anh đây rồi. Ảnh vừa tắt thở... Chúng tôi đang cố gắng cứu vãn..."
            jump badend
        label ontime:
            #ít hơn 4 điểm thời gian
            "May quá, có vẻ vẫn kịp."
            "Tôi chạy đến bên cạnh Lukase, tháo nắp an toàn ra, cầm chắc EpiPen rồi đặt đầu đen lên đùi anh ta."
            "Sau khi đã ổn định, tôi đẩy mạnh kim phun vào, nhẩm đếm năm giây rồi rút ra, đậy nắp lại."
            "Khoảng hai, ba phút sau đó."
            "Lukase dần tỉnh lại."
            mc "Ông ổn không đấy?"
            ld "Tôi… vẫn ổn."
            "Trông anh ta vô cùng yếu ớt và mệt mỏi, như thể giây tiếp theo sẽ lại ngất xỉu."
            ld "Cảm ơn ông. Có thể cho tôi… xin số liên lạc được không?"
            ld "Tôi muốn có dịp thì… mời ông đi ăn uống đâu đó… hậu tạ."
            menu:
                "Cho":
                    "Dù sao trông anh ta cũng thật tâm thật tình, cứ cho đi vậy."
                    mc "Ok, số của tôi là…"
                    ld "Cảm ơn ông."
                    mc "Mời chỗ nào không có món đậu phộng nhé."
                    ld "Haha… lâu lâu một lần vậy đủ tởn rồi."
                    $ lukase_affection += 3
                    #[+3 điểm thiện cảm Lukase.]
                    jump choice3_done
                "Không cho":
                    "Cũng không cần thiết lắm, và tôi không muốn dây vào phiền phức."
                    mc "Xin lỗi, không được."
                    ld "A, tôi hiểu… Dù sao cũng cảm ơn ông."
                    $ humanpoint += 1
                    #[+1 điểm Human.]
                    jump choice3_done

        label badend:
            #Bad end cg?

        label choice3_done:
                "Giải quyết biến cố xong xuôi, tôi cứ thế tận hưởng bữa tiệc đến khi kết thúc."

    #Part 3
    # Có transition?
    scene room #phòng Nhânn
    "Một ngày đẹp trời cuối năm, cái lạnh mùa đông đã dần bao phủ khắp thành phố."
    "Lễ Giáng sinh vẫn còn cách hai tuần, nhưng tâm trạng của người đi làm có vẻ trở nên đình trệ hẳn."
    "Những lúc này tôi rất dễ yếu lòng trước những lời mời tụ tập đàn đúm…"
    rb "Nhânn, ra cà phê không?"
    "Là Richhard, ‘nhà phát minh thiên tài’ của tiệm sửa xe, bạn đại học của tôi."
    mc "Ok, nổ địa chỉ đi."
    "Cậu ta canh rất đúng lúc để rủ rê đó. Giờ nghỉ trưa những ngày này được Sếp cho phép kéo dài hơn bình thường."
    "Tôi đã nghĩ đó là một buổi tụ tập thắt chặt tình đồng chí, cho đến khi thấy bóng người vừa quen vừa lạ ngồi cạnh anh ta."
    "Kính chống nắng, khẩu trang cùng style quần áo khác hẳn với hình tượng trong mắt công chúng để chống lại sự soi mói của paparazzi."
    "Đó là Shine, ca sĩ kiêm guitarist của nhóm nhạc rock Love Tender siêu hot hiện nay."
    rb "Nghĩaa không đi với ông hả?"
    "Thay vì giải thích tại sao cô idol kia lại ở đây, Richhard quyết định hỏi tôi về sự vắng mặt của một người khác."
    mc "Ông có bảo tui rủ ảnh đâu."
    rb "Tưởng hai người hay đi chung, ai biết đâu."
    mc "Ông rủ ngay ngày đi làm đó."
    rb "Đang nghỉ trưa mà?"
    mc "Thì ảnh cũng đang vùi đầu trong deadline thôi. Khỏi cần hỏi."
    "Đời designer khó nuốt hơn Richhard nghĩ nhiều. Nếu ai thích tiền, thích đau cột sống thì mời ngồi xuống nếm bốn chữ ‘hào quang rực rỡ’ để biết nó là gì."
    mc "Elizabeth đệ tứ đâu? Ông không dẫn nó theo à?"
    rb "Chỗ này mà không cấm thì tui đã dẫn cả một dàn Elizabeth đệ tứ theo luôn rồi."
    "À. Nỗi đau của con sen."
    mc "Cấm cũng được, đỡ lộn xộn."
    mc "Mà tiệm này… cái gì cũng tốt, mỗi tội chả bao giờ chịu cập nhật cái kệ đựng báo."
    "Tôi nhìn cái kệ chất mấy số tạp chí, báo giấy đã có tuổi còn hơn đống đồ dơ nhà Nghĩaa."
    rb "Tầm này ai thèm đọc báo giấy nữa, chuyển qua online hết rồi."
    th "Ừ, tui cũng toàn lướt điện thoại, chẳng có nhớ lần cuối rảnh rỗi đọc sách báo giấy là khi nào rồi."
    menu:
            "Hỏi thăm Richhard":
                mc "Thế tiệm sửa xe của ông như nào rồi?"
                rb "Vẫn thế."
                rb "Dạo này người ta khuyến khích dùng phương tiện công cộng nhiều nên cũng hơi oải."
                mc "Thì tiền kiếm được bao nhiêu là đổ vào mấy cái phát minh hết chứ gì."
                "Dù sao cũng là bạn từ nhỏ, tôi cũng không ngại mà nói thẳng."
                rb "Ha ha, đam mê mà, biết sao giờ."
                th "Tui thấy Richhard rất tuyệt đó, có thể tự do làm điều mình thích bất chấp mọi thứ."
                th "Mà cũng phải giỏi thế nào mới phát minh được nhiều thứ hay ho vậy."
                rb "Cậu thực sự rất phát minh của tui hay hả?"
                "Gương mặt Richhard sáng bừng trước lời khen."
                th "Ừ. Lần trước cậu cho tui xem giày tìm đường cho vịt rất là ấn tượng luôn."
                "Tôi thì thấy liều lĩnh như cậu ta không xem là giỏi được, nhưng ghi được điểm trong mắt người đẹp thì tốt cho Richhard."
                mc "Thế, dạo này ông với 'ai kia’ có gì mới chưa?"
                "Tôi huých nhẹ cùi chỏ lên cánh tay cậu bạn, nửa đùa nửa thật."
                rb "Hả?"
                "Gương mặt Shine cũng không có biểu cảm gì cho thấy cô nàng biết mình là đối tượng trong câu hỏi đó."
                "Người bị hỏi ngơ ngác, người được nhắc đến cũng ngơ ngác."
                "Xem ra vẫn chưa có tiến triển gì."
                jump choice4_done

            "Hỏi thăm Shine":
                mc "Hôm nay idol nhà ta ăn mặc đáng yêu hơn bình thường nhiều nha."
                "Vừa dứt lời, tôi đã bị Richhard 'lườm yêu' một cái."
                "Phải mà trong chuyện tỏ tình cậu ta cũng nhanh nhẹn thế."
                "Vì Shine rất nổi tiếng với giới trẻ nên khi gặp nhau, chúng tôi gọi cổ bằng tên thật là Hikkari để không bị lộ."
                mc "Dạo này cậu thế nào rồi, có thông tin gì về việc ra album solo không?"
                th "Thôi thôi… Không có scandal là tui mừng lắm rồi."
                th "Dù là được ra album cá nhân thì thu nhập sẽ tốt hơn, nhưng…"
                mc "Cậu nhiều fan như vậy, sớm muộn gì công ty cũng sẽ cân nhắc thôi."
                th "À mà… khoe nhẹ tí là tui sắp đi lưu diễn đó."
                mc "Ồ? Chúc mừng cậu!"
                mc "Mà hai nhóc sinh đôi nhà cậu đâu?"
                th "Nay tụi nhỏ đi ngoại khóa với lớp rồi."
                "Richhard vẫn đang nhìn chúng tôi chăm chú từ nãy đến giờ."
                "Có vẻ cậu ta muốn chen vô nói lắm, nhưng mà mù tịt về showbiz nên chỉ biết ngồi nghe."
                "Đến chịu với ông tướng này, muốn cua người ta thì phải đầu tư hơn về chất xám chứ."
                "Bây giờ dù Shine thực sự đang có ý với Richhard, thì giữa hai người có khoảng cách lớn vậy cũng khó lòng mà bên nhau được."
                jump choice4_done

    label choice4_done:
        #...
    "Rõ ràng là chuyện người mù cũng thấy, mà nhân vật chính thì cả đôi ngờ nghệch chẳng ai nhận ra."
    "Để tôi kể rõ hơn về lý do mà mình cho rằng Shine và Richhard xứng là một đôi."
    "Cho mọi người thấy không phải là ông bạn tôi đơn phương người đẹp."
    "Cái phát minh giày tìm đường cho vịt mà Shine khen ban nãy…"
    "Chính là một thất bại của tạo hoá."
    "Richhard có nuôi một con vịt tên Elizabeth đệ tứ."
    "Cậu ta chế cho con vịt của mình một đôi dép có kết nối với thiết bị điều khiển."
    "Khi con vịt chạy lạc mà cậu ta không tìm được nữa, thì chỉ cần đặt lộ trình trên thiết bị điều khiển."
    "Đôi giày sẽ tự đưa con vịt đến địa điểm vừa cài đặt."
    "Tuy nhiên, cái này có nhược điểm là nếu con vịt không muốn đi và rướn về hướng ngược lại thì sẽ làm đau nó."
    "Vì vậy Richhard đã làm một cái chốt mở tự động, để khi con vịt cố vùng vẫy sẽ thoát được khỏi đôi giày."
    "Cuối cùng vịt một nơi, dép một nẻo."
    "Vậy là phát minh hay dữ chưa?"
    "Nhưng Shine thì luôn thấy ấn tượng trước những giải pháp giải quyết vấn đề vốn không tồn tại của Richhard."
    "Vậy mà cả hai vẫn chưa nhận ra tình cảm của đối phương."
    "Tôi chả hiểu cái bọn yêu nhau nghĩ gì luôn…"

    "Có lẽ là do lần đầu gặp nhau của hai đứa này đầy drama nên đường tình cũng trắc trở."
    "Tầm 6 tháng trước…"
    "Hôm đó vừa tan làm thì Richhard đã gọi điện rủ tôi đến quán cà phê vì họ mới ra mắt cà phê vị sầu riêng dưa hấu."
    "Mấy cái lạ lạ khác thường thì làm sao thiếu mặt tên này được."
    "Nhờ vậy mà tình cờ gặp phải cô nàng thần tượng nổi tiếng Shine cũng đang đứng xếp hàng."
    "Khá thích nhạc của Love Tender, cộng thêm bản năng người trong nghề nên ít nhiều tôi cũng nhận ra ngay."
    "Thường mấy paparazzi vẫn sẽ theo sát người nổi tiếng bất kể ngày giờ."
    "Còn săn tin nghệ sĩ không phải mảng chuyên biệt của tôi."
    "Nếu cô ấy đang muốn có một buổi chiều yên ổn thì tôi sẽ không làm phiền."
    "Richhard đề nghị ra công viên để vừa tản bộ vừa thưởng thức cà phê."
    "Tôi cũng muốn hít tí khí trời vì cả ngày đã ngồi dí trong tòa soạn rồi nên đồng ý."
    "Trong lúc xếp hàng, tôi nhìn lung tung xung quanh xem thử các khách hàng khác."
    "Lọt vào tầm mắt là một cô gái trẻ đội mũ lưỡi trai, đeo máy ảnh trước ngực."
    "Trên tay cô là một tờ báo, tiêu đề to tướng là mẩu tin nhà hàng Grandelius mất điện."
    "Có gã đàn ông kéo hoodie trùm kín mặt cắm đầu vào điện thoại, cũng đang đứng đợi đồ ăn."
    "Và một bà mẹ ngồi ăn với cậu con trai nhỏ."
    "Sau khoảng thời gian chờ đợi 'hạnh phúc', cuối cùng cà phê của chúng tôi cũng xong."
    "Tôi theo Richhard mang da công viên MegaLawn, chẳng  ngờ lại bị người nổi tiếng chặn đường."
    th "Cậu… Đưa ảnh chụp lén cho tui!"
    th "Lại còn theo đến tận đây. Mấy tấm kia chưa đủ sao?"
    "Có lẽ vì tôi vẫn đang đeo thẻ phóng viên do từ chỗ làm ra, cổ còn đeo máy ảnh…"
    "Nên Shine đã nghĩ tôi là paparazzi theo mình săn tin."
    "Người nổi tiếng như có bản năng nhận diện phóng viên ấy nhỉ."
    mc "Cô bình tĩnh chút đi đã. Tôi không có chụp gì hết, không tin thì cô cứ xem đi."
    "Tôi liền mở thư mục ảnh trong máy mình ra cho cô ấy xem để chứng minh."
    "Shine nhíu mày, nhưng chăm chú quan sát một hồi rồi thì thốt lên."
    th "A… Xin lỗi."
    "Gương mặt cô cũng dãn ra, không còn căng thẳng như ban nãy."
    th "Lúc nãy tui thấy có ánh đèn flash loé lên, cứ tưởng lại bị theo dõi."
    th "Thường thì phóng viên chỉ chụp từ xa, còn mấy người bám đuôi nguy hiểm lắm…"
    menu:
        "Đúng là có stalker.":
            "Dù sao cũng là người trong ngành, tôi nhanh chóng nhận ra vấn đề."
            "Nếu là đèn flash thì không thể nhầm được."
            "Kẻ theo dõi đã rình rập từ lúc ở quán ăn rồi."
            "Chính là…"
            #["Là tên đội mũ trùm khả nghi?" | "Là bà mẹ dắt theo đứa con?" | "Là cô gái đọc báo?"]

        "Cô nhìn nhầm rồi.":
            mc "Chắc cô nhìn nhầm rồi, có khi ai đang chụp hình đồ uống check-in thôi."
            "Thời buổi sống ảo mà, ra cửa tiệm mua đồ uống mới ra để chụp hình khoe không có gì lạ."
            th "A… Vậy cho tui xin lỗi nha…"
            "Tôi cũng định bỏ qua rồi, nhưng lúc này Richhard chợt lên tiếng."
            rb "Người khả nghi à?"
            rb "Chẳng phải người kia đang thập thò y chang thằng Nhânn lúc làm việc sao?"
            "Tôi toan lên tiếng phản bác vụ cậu ta so sánh stalker với mình, nhưng rồi cũng ngậm miệng lại."
            "Người ở hướng Richhard đang chỉ là…"
            #["Là tên đội mũ trùm khả nghi?" | "Là bà mẹ dắt theo đứa con?" | "Là cô gái đọc báo?"]

    label choice4:
        menu:
            "Là tên đội mũ trùm khả nghi?" if not stalker1:
                $ stalker1 = True
                "Tên đội mũ trùm trong quán cà phê có vẻ khả nghi. Là hắn sao?"
                "Tôi quay đầu lại nhìn, chỉ thấy một cô gái đội mũ lưỡi trai."
                "Không có bóng người nào giống như tên đó quanh đây cả."
                $ humanpoint += 1
                #[+1 điểm Human.]
                #quay lại chọn tiếp

            "Là bà mẹ dắt theo đứa con?" if not stalker2:
                $ stalker2 = True
                "Đi theo dõi người khác còn dắt theo con nhỏ? Thật vô lý."
                "Chắc chắn không thể là họ."
                $ humanpoint += 1
                #[+1 điểm Human.]
                #quay lại chọn tiếp

            "Là cô gái đọc báo?":
                "Là cô gái đeo máy ảnh cầm tờ báo!"
                jump choice5_done

    label choice5_done:
        #...
    "Chuyện ở nhà hàng Grandelius xảy ra vào tháng hai, bây giờ lại là tháng sáu rồi."
    "Ai lại đi đọc báo của bốn tháng trước cơ chứ?"
    "Lại còn mang theo máy ảnh?"
    "Hai chuyện khả nghi trùng hợp cùng hội tụ trên một người, quá mức hi hữu."
    "Tờ báo kia có lẽ là do cửa hàng lười đổi như mọi khi, rồi gặp người không thật sự có ý đọc báo cầm trúng."
    "Suy luận xong, tôi vội vàng bước đến và tóm lấy tay cô gái một cách mạnh bạo."
    mc "Cô đang làm gì đó?"
    mc "Nếu cố tình theo dõi và gây bất lợi, chúng tôi sẽ báo cảnh sát đấy."
    "Có lẽ là sợ hãi trước lời đe dọa của tôi, cô vội vàng lấy thẻ nhà báo ra, cuống quýt giải thích rằng mình chỉ là thợ săn ảnh mới vào nghề, không có ý xấu."
    "Quan điểm khác biệt, tôi vốn chẳng hòa thuận gì với hội paparazzi."
    "Phóng viên mảng đời sống như tôi chỉ săn tin người nổi tiếng khi họ tham gia các sự kiện cộng đồng."
    "Nhưng trong ngành này, người nổi tiếng cũng hiếm khi thật sự đâm đơn kiện paparazzi."
    "Dù sao chỉ cần không phải tin bất lợi, việc bị chụp trúng cũng là một cách quảng bá, hâm nóng tên tuổi không tệ."
    "Mà cô gái này rõ đúng là lính mới, vì paparazzi thường chỉ săn ảnh từ xa, như một thoả thuận ngầm."
    "Để làm phiền nghệ sĩ và phá hỏng hòa khí hai bên."
    "Nể tình đàn em vừa vào ngụp lặn trong cái ngành moi chuyện thiên hạ đem về làm của mình, tôi cũng muốn giúp cô gái dàn xếp."
    "Tôi quyết định thử hỏi Shine xem có thể thông cảm giúp không."
    "Với điều kiện là cô nàng xóa hết ảnh hôm nah chụp và hứa không theo dõi riêng tư thế này nữa."
    aa4 "Em, em xin lỗi! Em sẽ không stalk chị nữa đâu, xin chị bỏ qua cho em."
    aa4 "Em đã biết mình nên làm gì rồi!"
    "Dù có giọng ca khủng đầy nội lực cùng hình tượng ngầu đét trên sân khấu, Shine thực ra khá hiền hoà."
    "Thấy người kia thành tâm phục thiện, cô cũng dịu giọng."
    th "Ừm… được rồi, bỏ qua đi. Lần sau đừng vậy nữa…"
    "Nói xong thì có chút ngại ngùng quay sang tôi và Richhard."
    th "C-cảm ơn hai cậu… Và cũng xin lỗi lần nữa chuyện ban nãy nha."
    "Cô ấy chắc vẫn ngại vì hiểu lầm tôi, nhưng thái độ giải quyết nhanh gọn này thì chắc không phải lần đầu Shine bị theo dõi."
    mc "Không có gì đâu. Cẩn thận một chút  tốt mà."
    th "Ừm…"
    "Shine toan rời đi thì Richhard bên cạnh tôi đã lên tiếng."
    rb "Tui thấy bạn rất dễ thương. Có thể làm bạn bè không?"
    rb "Lần tới có đi chơi thì rủ tui theo, tui sẽ đảm bảo an toàn cho bạn."
    "Tôi há hốc mồm ra trước sự vô tri của cậu ta, và cô idol đằng kia trông cũng bối rối không kém."
    th "A… vâng…"
    th "C-Cũng được…"
    "Có thể nhìn ra được, sự đồng ý này bắt nguồn từ lòng cảm kích và phần nhiều là lịch sự."
    "Thế mà tên đầu gỗ nào đó lại tưởng thật, còn hỏi cả code liên lạc."
    rb "Tui đánh nhau giỏi lắm. Gặp rắc rối có thể tìm tui giúp đó!"
    th "C-Cái này… thì không cần tới mức đó đâu ha."
    "G-Giải cứu Shine thôi!"
    "Thấy vậy, tôi đành bước tới ngăn Richhard trước khi cậu ta tự làm mình trông như một stalker thực thụ."
    th "Ừm… Cảm ơn vì ý tốt."
    th "Có duyên gặp lại."
    rb "Chắc chắc sẽ gặp mà!"
    "Richhard, não ông chập chỗ nào rồi!!!"
    scene bg room #thay bằng file background hiện tại
    with dissolve
    "Lần này thì Shine đã thành công rời đi thật."
    mc "Lần đầu gặp mà dồn dập vậy, trông ông còn khả nghi hơn cả cô kia đó."
    mc "Đến tui còn sợ."
    rb "Thì hồi đi học toàn vậy mà?"
    mc "Haiz. Đúng là văn hóa khác biệt."
    "Nhưng có vẻ không nể lời tôi nói ra gì, những lần sau đó tình cờ gặp lại Shine ở quanh điểm cũ, Richhard vẫn cứ hớn hở tiến lại chào hỏi người ta như thể thân thiết lắm."
    "Và không ý tứ mà gọi to nghệ danh của người ta."
    "Đến mức cô ca sĩ phải bảo cậu ta gọi thẳng tên thật để tránh bị lộ."
    th "Tên thật của tui là Toumato Hikkari. Có thể gọi thay nghệ danh nha…"
    rb "Họ của cậu nghe như quả cà chua á, đọc lên nghe buồn cười ghê. Tui gọi là Hikkari thôi được không?"
    th "... Thôi được rồi."
    "Nhất Richhard. Fan đu idol cũng không được như tên này đâu."
    "Sau này, có lần xe chở ban nhạc Love Tender bị hỏng giữa đường lúc nửa đêm."
    "Trong lúc quản lý đứng bên ngoài xe than thở tìm thợ sửa, tôi, Richhard và Nghĩaa vừa đi nhậu ngang qua."
    "Thoáng thấy Shine gần đó, cậu chàng liền tới chào hỏi, hoàn toàn không thèm bận tâm đến sự ngăn cản của tôi."
    "Cũng không thèm để vào mắt động thái chặn lại của vệ sĩ bên đó, ỷ sức trâu mà trực tiếp khống chế người ta."
    rb "Anh làm gì vậy, tui sợ à nha?"
    "... Tôi có thể giả vờ không quen tên này không?"
    "Nghĩaa cũng nhìn cậu ta bằng ánh mắt vô cùng phán xét."
    "Cũng may Shine vội vàng đứng ra can ngăn, bảo với họ Richhard là 'bạn' mình để tránh rắc rối."
    "Từ đó tụi tôi thành bạn của idol nổi tiếng luôn."
    rb "Sao mọi người lại dừng xe giữa đường đó?"
    th "Xe hỏng rồi… Mà đêm hôm thế này tìm thợ cũng khó, nên bọn tui đang định gọi xe taxi."
    rb "Tui là thợ sửa xe nè, hay là để xem thử?"
    "Sau khi Shine thảo luận với quản lý, ổng mừng rỡ để Richhard xem qua chiếc xe."
    hn "Crush nó đấy à?"
    mc "Anh cũng thấy hả? Vậy mà nó không nhận ra mình thích người ta đó."
    hn "Còn lạ gì nữa. Richhard mà, toàn làm mấy chuyện ngớ ngẩn."
    mc "Người ta cũng tử tế quá, phải bình thường chắc nó lên đồn uống trà vì quấy rối rồi."
    hn "Thật ra, đôi khi người quá hướng nội gặp trúng người hướng ngoại thân thiện, thì họ dễ cảm động lắm."
    "Tôi có chút ngạc nhiên trước câu này."
    hn "Thì bản thân anh vốn khó kết bạn, nếu chú không chủ động sấn tới, anh cũng không nghĩ sẽ chơi chung được như này."
    mc "Tự nhiên vừa tự hào vừa tổn thương."
    hn "Nhưng mà nhiệt tình quá có khi lại thành phiền, thậm chí còn thấy sợ nữa."
    mc "Cũng đúng. Mà trong giới vừa cạnh tranh khắc nghiệt vừa lắm âm mưu dương mưu, tìm được người thật thà không vụ lợi như Richhard cũng khó."
    mc "Chắc vì vậy nên Shine mới dễ mở lòng hơn."
    hn "Nhìn người ta sửa xe chăm chú ghê, có khi nào cổ cũng thích thằng nhỏ không?"
    mc "Không thể nào."
    rb "Sửa xong rồi."
    "Tôi quay đầu nhìn thấy cậu ta đang cười rộ lên, cả người giống như phát ra ánh sáng hớp hồn."
    mc "... Thằng ngố này vậy mà nguy hiểm phết."
    hn "Hay là anh cũng học tán tỉnh thử?"
    mc "Cứ dùng mấy mẫu câu thả thính trending thì anh làm trai tân đến chết luôn cho xem."
    hn "Chú mày chờ đó."
    "Trong lúc chúng tôi tám nhảm, Richhard đã tạm biệt những người bên kia và quay lại."
    "Thấy vậy, tôi với Nghĩaa cũng chào xã giao một chút, rồi hai bên đường ai nấy đi."
    "Richhard hớn hở chìa điện thoại ra khoe với chúng tôi số danh bạ tên 'Hikkari'."
    "Nhưng nụ cười đắc thắng của cậu ta làm tôi cứ có cảm giác cách tiếp cận này sai sai."

    #[Hiện tại]
    "Hoặc là không."
    "Nhìn vào mối quan hệ lúc này của bọn họ, ai mà ngờ được cậu ta từng làm những chuyện ngớ ngẩn vậy chứ."
    "Trò chuyện thêm một lúc, Shine thông báo rằng đến giờ tập thể dục của cô, nên ba chúng tôi quyết định rời khỏi quán cà phê."
    "Vừa ra khỏi cửa, bỗng có người chạy ngang qua đụng phải Shine, khiến cô ca sĩ chuếnh choáng sắp ngã."
    menu:
        "Đỡ":
            "Tôi thuận tay đỡ lấy cô ấy."
            "Song chợt nhìn thấy cái nhíu mày của ai kia, tôi vội vàng thả ra, khiến cả hai cùng loạng choạng."
            "Richhard vội tiến đến đỡ Shine, còn tôi thì phải tự dựa vô cái cửa gần đó trước khi đo sàn."
            "Lòng tốt của tôi đặt sai chỗ rồi. Đáng ra nên để mặc đôi chim câu đó tự chơi với nhau."
            "Nhìn xem, cảnh tượng tình tứ thế này, không làm vài nháy thì đúng là có lỗi với tổ nghề."
            "Nghĩ là làm, tôi giơ máy ảnh lên, chụp lại khung cảnh màu hồng trước mặt."
            "Đến khi Shine ngượng ngùng đẩy nhẹ Richhard ra, cậu ta vẫn chưa hoàn hồn."
            "Cô ấy tạm biệt rồi đi khuất, bầu không khí gượng gạo vẫn còn lửng lơ đâu đây."
            "Richhard đột nhiên quay sang ngửi ngửi tôi và nhăn mặt."
            mc "Bị gì đó?"
            rb "Ông có mùi khó ngửi ghê."
            "Không hiểu sao lại bị chê ngang hông, tôi trợn cả mắt lên."
            rb "Nãy Hikkari có mùi thơm lắm."
            mc "Ừ thơm thật."
            "Vừa dứt lời, cổ áo tôi đã bị cậu ta túm lấy."
            rb "Ông lợi dụng lúc cổ ngã làm gì rồi, hả?"
            "Hết cứu, thằng nào yêu vào cũng ngu đi vậy à?"
            jump choice5_done #nếu sau đó không còn gì

        "Để Richhard đỡ":
            "Tôi nhanh trí huých một cái, đẩy cậu chàng lên đỡ lấy cô."
            "Hệt như phim anh hùng cứu mỹ nhân luôn."
            "Nhìn xem, cảnh tượng tình tứ thế này, không làm vài nháy thì đúng là có lỗi với tổ nghề."
            "Nghĩ là làm, tôi giơ máy ảnh lên, chụp lại khung cảnh màu hồng trước mặt."
            "Vì xung quanh đông người, sau khi ngượng ngùng đẩy Richhard ra, Shine cũng vội cáo bận rồi chạy đi, để lại một tên ngố thẫn thờ nhìn theo."
            "Đột nhiên, tên ngố đó quay sang ngửi ngửi tôi và nhăn mặt."
            mc "Bị gì đó?"
            rb "Mùi của con gái thơm ghê."
            mc "Cái thằng suốt ngày sống với mùi dầu máy như ông, ngửi cái gì chả thơm."
            rb "Ông có thơm đâu?"
            "Ủa tự nhiên bị chê ngang hông? Tên này chán sống rồi ha gì."
            $ TH_event += 1
            #[+1 điểm event TH.]
            rb "Ê mà, không được viết bài về vụ này đó."
            menu:
                "Không viết":
                    "Nghĩ lại thì vẫn đang là ngày nghỉ, nên tôi gật đầu với cậu ta."
                    "Không viết thì không viết."
                    "Tôi không viết, nhưng lại có người khác viết."
                    #chuyển cảnh
                    "Ngay hôm sau, trên báo đã nổ ra biến lớn với tấm ảnh Richhard ôm Shine và tiêu đề giật tít."
                    "'Idol nhạc Rock Shine đi dạo cùng bạn trai, tình tứ tại Mega Lawn'."
                    "Xét về chuyên môn mà nói thì vẫn chưa đủ 'đô' lắm, nhưng bản thân {i}sự việc{/i} đã đủ khiến bài báo đó nổi như cồn."
                    "Và như một hệ quả tất yếu, quản lý của Shine gọi đến hẹn gặp tôi."
                    "Đúng là nằm không cũng dính đạn."
                    "À, không hẳn là nằm không?"
                    "Dù sao thì, tôi đã rủ cả người có liên quan trực tiếp - cậu 'bạn trai tin đồn' nọ đi cùng."
                    #Công viên.
                    mc "Đúng là tôi có tình cờ chụp được và tính viết, nhưng bạn tôi trong ảnh đã ngăn lại rồi."
                    mc "Đây, hai người cứ xem đi."
                    "Tôi đưa ảnh trong máy cho họ xem."
                    #jump minigame
                    #Minigame tìm điểm khác biệt [Thành công | Thất bại]

                "Viết bài":
                    "Hiếm khi có tin hot hòn họt thế này, sao có thể nói bỏ là bỏ chứ."
                    "Che mặt Richhard lại là được, sẽ chẳng ai nhận ra cậu ta đâu."
                    "'Ngày bình thường của ngôi sao nhạc rock', rõ vô cùng bình thường."
                    "Bởi hình tượng ca sĩ Rock luôn tỏa ra chút gì đó ngầu ngầu lạnh lùng."
                    "Nên tôi chỉ muốn cho thấy một góc nhìn khác về Shine, thân thiện, ngại ngùng đáng yêu."
                    "Thế mà lại bị biên tập viên sửa cả tiêu đề lẫn nội dung, thêm mắm dặm muối làm."
                    "Tôi biết mình chơi ngu rồi."
                    "Từ 'ngôi sao nổi tiếng cũng rất thân thiện' thành 'chuyện tình bí mật của ngôi sao nổi tiếng'' là sao vậy?"
                    "Chuyện gì đến cũng sẽ đến, quản lý của Shine gọi đến hẹn gặp tôi."
                    $ humanpoint += 1
                    #[+1 điểm Human.]
                    #Công viên.
                    "Sau khi mở loa ngoài thương lượng, cuối cùng tôi cũng thuyết phục được biên tập viên cho gỡ bài với cái giá nửa tháng lương."
                    "Và một chầu trà sữa cho cả ban Đời sống mà mình nhờ năn nỉ phụ."
                    mc "Xin lỗi Shine vì hiểu lầm không đáng có này."
                    mc "Nếu cô cho phép, tôi sẽ viết một bài đính chính để giải quyết mọi chuyện."
                    "Được sự đồng ý của Shine, tôi bắt đầu chọn hướng triển khai bài viết tiếp theo."
                    menu:
                        "Biện hộ người giống người":
                            "Một bài đính chính người giống người nhanh chóng được đăng lên ngày hôm sau.."
                            "Cũng may, lúc xảy ra chuyện Shine đã hóa trang che chắn, phong cách cũng không giống trên sân khấu."
                            "Fan thấy khác nhau quá mới chịu tin là không phải."
                            "Scandal lắng xuống, tôi ứng cử vị trí chuyên viết bài ủng hộ Shine với giá ưu đãi để chuộc lỗi, và cô ấy đồng ý."
                            jump choice5_done

                        "Giải thích người trong ảnh là ai":
                            "Tôi quyết định công khai danh tính Richhard để giải thích rõ chuyện đã xảy ra hôm đó."
                            "Nhưng một bộ phận lớn người hâm mộ không tin."
                            "Họ cho rằng chuyện quá hy hữu."
                            "Quan trọng hơn là có vẻ Richhard trở thành tâm điểm bị công kích điên cuồng, có lẽ vì sự ghen ghét vì được chạm vào thần tượng của bọn họ…"
                            "Tôi vô cùng hối hận, nhưng không đủ dũng khí để đối mặt với cậu ấy."
                            "Và Richhard cũng không liên lạc với tôi nữa…"
                            "Tin tức cuối cùng tôi nghe được về cậu ấy, là khi cảnh sát thông báo Richhard bị đâm chết trước cửa tiệm sửa xe."
                            #[Bad Ending.]

    label minigame:
        # Cơ chế minigame

        #[Thành công]
        "Chỉ ra điểm khác nhau lớn nhất giữa bức ảnh trong máy và bài báo xong, tôi gọi cho biên tập viên."
        "Qua loa ngoài của điện thoại, đầu dây bên kia xác nhận bài báo đó do một đồng nghiệp khác viết."
        "Thế là tôi lại phải liên lạc với cô ấy."
        aa4 "Ừ đúng rồi, là tui đó. Hôm đó vô tình gặp được, đúng là hay không bằng hên."
        aa4 "Tin vừa lên đã hot luôn."
        mc "Người trong ảnh là bạn thân em đó chị hai ơi!"
        "Ôi cái lưng già của tôi…"
        "Nó đã phải còng xuống vì năn nỉ ỉ ôi thuyết phục mãi cô đồng nghiệp mới chịu gỡ bài."
        "Dĩ nhiên là kèm một chầu trà sữa cho cả ban Đời sống."
        "Sau đó là một bài đính chính người giống người."
        "Cũng may, lúc xảy ra chuyện Shine đã hóa trang che chắn, phong cách cũng không giống trên sân khấu."
        "Fan thấy khác nhau quá mới chịu tin là không phải."
        "Cô ca sĩ xin lỗi vì gây rắc rối cho chúng tôi, còn thằng bạn tôi từ hôm đó cũng có thiện cảm vượt bậc, đòi mời người ta đi ăn."
        "Shine cũng đồng ý, có lẽ vì ngại bản thân là người nổi tiếng nên ảnh hưởng người xung quanh."
        "Nhưng lỗi không phải chỉ có mỗi cô ấy, nên tôi đã ứng cử vị trí chuyên viết bài ủng hộ cô ấy với giá ưu đãi để chuộc lỗi."
        "Cuộc gặp hôm đó đã kết thúc bằng hai lời hứa giữa ba người chúng tôi."
        jump choice5_done

        #[Thất bại]
        "Trong lúc bối rối, tôi đã không thể chỉ ra sự khác nhau giữa góc độ và các chi tiết trong hai tấm ảnh."
        "Tình ngay lý gian, làm sao để thanh minh đây."
        "Tôi đành gọi điện cầu cứu biên tập viên."
        "Qua loa lớn, đầu dây bên đó không chỉ không đính chính hộ tôi, còn chẳng chấp nhận gỡ bài."
        "Cúp máy trong lo lắng, tôi quan sát sắc mặt ngày càng xấu đi của người quản lý."
        mc "Xin lỗi… Tôi sẽ nghĩ cách giải quyết…"
        "Nhưng phía đó có vẻ vô cùng bất bình và đe dọa sẽ kiện tòa soạn khiến tôi hoảng loạn cả lên."
        "Trong lúc hai bên có tranh cãi, Shine đã phải đứng ra giảng hòa."
        "Không ngờ rằng paparazzi không hề tha cho bất cứ khoảnh khắc nào của nghệ sĩ."
        "Tôi và cô ca sĩ đã tiếp tục dắt tay nhau lên báo, với tấm ảnh chụp mới cùng nghi vấn 'Ca sĩ nổi tiếng bắt cá hai tay'."
        "Cả tiêu đề lẫn nội dung đều vô cùng nhảm nhí."
        "Nhưng có lẽ fan cuồng của Shine dễ tin người hơn tôi nghĩ."
        "Hoặc… bọn họ chỉ cần một cái cớ để có thể chỉ trích thần tượng vì không thuộc về mình."
        "Hai ngày sau, thời sự đăng tin."
        "Ca sĩ Shine bị sát hại tại nhà riêng, nghi vấn là do fan cuồng ra tay."
        "... Chuyện quái gì đã xảy ra thế này."
        "Khoan… Như vậy thì, tính mạng của tôi cũng gặp nguy hiểm sao?"
        "Chuông cửa chợt vang lên. Chắc là bố đi làm về."
        "Tôi vừa ra mở cửa vừa tự nhủ."
        "Ngày mai tôi phải báo cảnh sát mới đ–…"
        #BadEnd

    label choice6_done:
        #...

    return
