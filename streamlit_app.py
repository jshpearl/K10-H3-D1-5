import streamlit as st
import random

# --- DANH SÁCH 20 ẢNH GIF CHÚC MỪNG ---
gif_urls = [
    "https://i.pinimg.com/originals/fc/d6/fb/fcd6fb686facbcaf97f4602e6be6e04c.gif",
    "https://i.pinimg.com/originals/63/fa/7b/63fa7b8ceef65ed89ffefd2a834811ff.gif",
    "https://i.pinimg.com/originals/24/86/37/248637585fe5c57890aea979eb38bbbf.gif",
    "https://i.pinimg.com/originals/06/a6/c0/06a6c008c8d9b9f98fdf583373e8d87b.gif",
    "https://i.pinimg.com/originals/e9/54/8f/e9548f99211cb5a4999a68c0ff6d2862.gif",
    "https://i.pinimg.com/originals/11/82/59/118259993924863bd3f6457da365e2ac.gif",
    "https://i.pinimg.com/originals/47/65/fb/4765fbd8b250194051468ec3a0085a12.gif",
    "https://i.pinimg.com/originals/87/62/b8/8762b8ed3f80980481df7d73afa2fcff.gif",
    "https://i.pinimg.com/originals/be/62/73/be627352f3f42519bb417efd5556eabf.gif",
    "https://i.pinimg.com/originals/4a/e1/5a/4ae15a7a77842a2111db77ce3a802114.gif",
    "https://i.pinimg.com/originals/70/88/dc/7088dcfbb6d5004f62a260264d99ed2d.gif",
    "https://i.pinimg.com/originals/6b/c6/ed/6bc6edef34fb9e763f12aaf74b25310a.gif",
    "https://i.pinimg.com/originals/15/41/0f/15410fa493fdaf97e895647a102d9d5c.gif",
    "https://i.pinimg.com/originals/6f/d1/5a/6fd15a59ca0af6fddf6779ffbf050e82.gif",
    "https://i.pinimg.com/originals/64/04/94/640494359ff11c3f2d030ef92fcdd2f1.gif",
    "https://i.pinimg.com/originals/f1/52/0a/f1520a5ee03343c567532486a36c3c52.gif",
    "https://i.pinimg.com/originals/31/e6/54/31e654092894ecfc876acb0afb1e04cb.gif",
    "https://i.pinimg.com/originals/43/53/d9/4353d9a5aaa49d5c7ec509efff753f86.gif",
    "https://i.pinimg.com/originals/0e/f2/d2/0ef2d26098ce2477ee7c7ff1042164ce.gif",
    "https://i.pinimg.com/originals/37/55/2b/37552bf05549d4f67e45a646b586e94b.gif"
]

# --- 1. KHO DỮ LIỆU CHUẨN XÁC 300 TỪ HSK3 (GỘP TỪ FILE PDF + BỔ SUNG TỪ "低") ---
vocab_db = [
    {"h": "阿姨", "p": "āyí", "m": "Dì, cô"},
    {"h": "啊", "p": "a", "m": "A, á (thán từ)"},
    {"h": "矮", "p": "ǎi", "m": "Thấp"},
    {"h": "爱好", "p": "àihào", "m": "Sở thích"},
    {"h": "安静", "p": "ānjìng", "m": "Yên tĩnh"},
    {"h": "把", "p": "bǎ", "m": "Cây (lượng từ vật có cán) / Câu chữ bǎ"},
    {"h": "班", "p": "bān", "m": "Lớp"},
    {"h": "搬", "p": "bān", "m": "Dọn, rời, khiêng"},
    {"h": "办法", "p": "bànfǎ", "m": "Cách, biện pháp"},
    {"h": "办公室", "p": "bàngōngshì", "m": "Văn phòng"},
    {"h": "半", "p": "bàn", "m": "Một nửa, rưỡi"},
    {"h": "帮忙", "p": "bāngmáng", "m": "Giúp đỡ"},
    {"h": "包", "p": "bāo", "m": "Cặp, túi"},
    {"h": "饱", "p": "bǎo", "m": "No"},
    {"h": "北方", "p": "běifāng", "m": "Miền Bắc"},
    {"h": "被", "p": "bèi", "m": "Bị, được (bị động)"},
    {"h": "鼻子", "p": "bízi", "m": "Mũi"},
    {"h": "比较", "p": "bǐjiào", "m": "Tương đối, khá"},
    {"h": "比赛", "p": "bǐsài", "m": "Cuộc thi đấu"},
    {"h": "笔记本", "p": "bǐjìběn", "m": "Máy tính xách tay / Vở"},
    {"h": "必须", "p": "bìxū", "m": "Cần phải, bắt buộc"},
    {"h": "变化", "p": "biànhuà", "m": "Thay đổi"},
    {"h": "别人", "p": "biéren", "m": "Người khác"},
    {"h": "冰箱", "p": "bīngxiāng", "m": "Tủ lạnh"},
    {"h": "不但...而且...", "p": "búdàn...érqiě...", "m": "Không những... mà còn"},
    {"h": "菜单", "p": "càidān", "m": "Thực đơn"},
    {"h": "参加", "p": "cānjiā", "m": "Tham gia"},
    {"h": "草", "p": "cǎo", "m": "Cỏ"},
    {"h": "层", "p": "céng", "m": "Tầng, lớp"},
    {"h": "差", "p": "chà", "m": "Kém, thiếu"},
    {"h": "超市", "p": "chāoshì", "m": "Siêu thị"},
    {"h": "衬衫", "p": "chènshān", "m": "Áo sơ mi"},
    {"h": "成绩", "p": "chéngjì", "m": "Thành tích"},
    {"h": "城市", "p": "chéngshì", "m": "Thành phố"},
    {"h": "迟到", "p": "chídào", "m": "Đến muộn"},
    {"h": "除了", "p": "chúle", "m": "Ngoài... ra"},
    {"h": "船", "p": "chuán", "m": "Thuyền, tàu"},
    {"h": "春天", "p": "chūntiān", "m": "Mùa xuân"},
    {"h": "词典", "p": "cídiǎn", "m": "Từ điển"},
    {"h": "聪明", "p": "cōngming", "m": "Thông minh"},
    {"h": "打扫", "p": "dǎsǎo", "m": "Quét dọn"},
    {"h": "打算", "p": "dǎsuàn", "m": "Kế hoạch, dự định"},
    {"h": "带", "p": "dài", "m": "Mang theo"},
    {"h": "担心", "p": "dānxīn", "m": "Lo lắng"},
    {"h": "蛋糕", "p": "dàngāo", "m": "Bánh kem"},
    {"h": "当然", "p": "dāngrán", "m": "Đương nhiên"},
    {"h": "地", "p": "de", "m": "Trợ từ (sau trạng ngữ)"},
    {"h": "灯", "p": "dēng", "m": "Đèn"},
    {"h": "低", "p": "dī", "m": "Thấp"}, 
    {"h": "地方", "p": "dìfang", "m": "Chỗ, nơi"},
    {"h": "地铁", "p": "dìtiě", "m": "Tàu điện ngầm"},
    {"h": "地图", "p": "dìtú", "m": "Bản đồ"},
    {"h": "电梯", "p": "diàntī", "m": "Thang máy"},
    {"h": "电子邮件", "p": "diànzǐ yóujiàn", "m": "Email"},
    {"h": "东", "p": "dōng", "m": "Phía đông"},
    {"h": "冬天", "p": "dōngtiān", "m": "Mùa đông"},
    {"h": "动物", "p": "dòngwù", "m": "Động vật"},
    {"h": "短", "p": "duǎn", "m": "Ngắn"},
    {"h": "段", "p": "duàn", "m": "Đoạn, khoảng"},
    {"h": "锻炼", "p": "duànliàn", "m": "Tập thể dục"},
    {"h": "多么", "p": "duōme", "m": "Biết bao nhiêu"},
    {"h": "饿", "p": "è", "m": "Đói"},
    {"h": "耳朵", "p": "ěrduo", "m": "Tai"},
    {"h": "发", "p": "fā", "m": "Gửi, phát"},
    {"h": "发烧", "p": "fāshāo", "m": "Sốt"},
    {"h": "发现", "p": "fāxiàn", "m": "Phát hiện"},
    {"h": "方便", "p": "fāngbiàn", "m": "Thuận tiện"},
    {"h": "放", "p": "fàng", "m": "Đặt, để"},
    {"h": "放心", "p": "fàngxīn", "m": "Yên tâm"},
    {"h": "分", "p": "fēn", "m": "Phút, xu, điểm"},
    {"h": "附近", "p": "fùjìn", "m": "Vùng lân cận"},
    {"h": "复习", "p": "fùxí", "m": "Ôn tập"},
    {"h": "干净", "p": "gānjìng", "m": "Sạch sẽ"},
    {"h": "感冒", "p": "gǎnmào", "m": "Bị cảm"},
    {"h": "感兴趣", "p": "gǎn xìngqù", "m": "Có hứng thú, thích"},
    {"h": "刚才", "p": "gāngcái", "m": "Lúc nãy"},
    {"h": "个子", "p": "gèzi", "m": "Vóc dáng"},
    {"h": "根据", "p": "gēnjù", "m": "Căn cứ vào"},
    {"h": "跟", "p": "gēn", "m": "Cùng, với"},
    {"h": "更", "p": "gèng", "m": "Càng, hơn nữa"},
    {"h": "公斤", "p": "gōngjīn", "m": "Kilogram"},
    {"h": "公园", "p": "gōngyuán", "m": "Công viên"},
    {"h": "故事", "p": "gùshi", "m": "Truyện, câu chuyện"},
    {"h": "刮风", "p": "guāfēng", "m": "Nổi gió"},
    {"h": "关", "p": "guān", "m": "Đóng, tắt"},
    {"h": "关系", "p": "guānxi", "m": "Quan hệ"},
    {"h": "关心", "p": "guānxīn", "m": "Quan tâm"},
    {"h": "关于", "p": "guānyú", "m": "Về, liên quan đến"},
    {"h": "国家", "p": "guójiā", "m": "Quốc gia, đất nước"},
    {"h": "过", "p": "guò", "m": "Trải qua, ăn mừng"},
    {"h": "过去", "p": "guòqù", "m": "Quá khứ"},
    {"h": "还是", "p": "háishì", "m": "Hay là"},
    {"h": "害怕", "p": "hàipà", "m": "Sợ hãi"},
    {"h": "黑板", "p": "hēibǎn", "m": "Bảng đen"},
    {"h": "后来", "p": "hòulái", "m": "Sau đó"},
    {"h": "护照", "p": "hùzhào", "m": "Hộ chiếu"},
    {"h": "花(n)", "p": "huā", "m": "Hoa"},
    {"h": "花(v)", "p": "huā", "m": "Tiêu tốn"},
    {"h": "画", "p": "huà", "m": "Vẽ, bức tranh"},
    {"h": "坏", "p": "huài", "m": "Hỏng, xấu"},
    {"h": "欢迎", "p": "huānyíng", "m": "Hoan nghênh"},
    {"h": "还", "p": "huán", "m": "Trả lại"},
    {"h": "环境", "p": "huánjìng", "m": "Môi trường"},
    {"h": "换", "p": "huàn", "m": "Đổi, thay thế"},
    {"h": "回答", "p": "huídá", "m": "Trả lời"},
    {"h": "会议", "p": "huìyì", "m": "Hội nghị, cuộc họp"},
    {"h": "或者", "p": "huòzhě", "m": "Hoặc là"},
    {"h": "几乎", "p": "jīhū", "m": "Hầu như"},
    {"h": "机会", "p": "jīhuì", "m": "Cơ hội"},
    {"h": "极(了)", "p": "jí(le)", "m": "Cực kỳ, hết sức"},
    {"h": "记得", "p": "jìde", "m": "Nhớ, còn nhớ"},
    {"h": "季节", "p": "jìjié", "m": "Mùa"},
    {"h": "检查", "p": "jiǎnchá", "m": "Kiểm tra, khám"},
    {"h": "简单", "p": "jiǎndān", "m": "Đơn giản"},
    {"h": "见面", "p": "jiànmiàn", "m": "Gặp mặt"},
    {"h": "健康", "p": "jiànkāng", "m": "Khỏe mạnh"},
    {"h": "讲", "p": "jiǎng", "m": "Giải thích, nói"},
    {"h": "教", "p": "jiāo", "m": "Dạy"},
    {"h": "角", "p": "jiǎo", "m": "Hào (tiền)"},
    {"h": "脚", "p": "jiǎo", "m": "Bàn chân"},
    {"h": "接", "p": "jiē", "m": "Đón"},
    {"h": "街道", "p": "jiēdào", "m": "Đường phố"},
    {"h": "节目", "p": "jiémù", "m": "Chương trình"},
    {"h": "节日", "p": "jiérì", "m": "Ngày lễ"},
    {"h": "结婚", "p": "jiéhūn", "m": "Kết hôn"},
    {"h": "结束", "p": "jiéshù", "m": "Kết thúc"},
    {"h": "解决", "p": "jiějué", "m": "Giải quyết"},
    {"h": "借", "p": "jiè", "m": "Mượn, vay"},
    {"h": "经常", "p": "jīngcháng", "m": "Thường xuyên"},
    {"h": "经过", "p": "jīngguò", "m": "Đi qua"},
    {"h": "经理", "p": "jīnglǐ", "m": "Giám đốc"},
    {"h": "久", "p": "jiǔ", "m": "Lâu dài"},
    {"h": "旧", "p": "jiù", "m": "Cũ"},
    {"h": "句子", "p": "jùzi", "m": "Câu"},
    {"h": "决定", "p": "juédìng", "m": "Quyết định"},
    {"h": "可爱", "p": "kě'ài", "m": "Đáng yêu"},
    {"h": "渴", "p": "kě", "m": "Khát"},
    {"h": "刻", "p": "kè", "m": "15 phút, khắc"},
    {"h": "客人", "p": "kèrén", "m": "Khách"},
    {"h": "空调", "p": "kōngtiáo", "m": "Điều hòa"},
    {"h": "口", "p": "kǒu", "m": "Miệng, miếng"},
    {"h": "哭", "p": "kū", "m": "Khóc"},
    {"h": "裤子", "p": "kùzi", "m": "Cái quần"},
    {"h": "筷子", "p": "kuàizi", "m": "Đũa"},
    {"h": "蓝", "p": "lán", "m": "Màu xanh da trời"},
    {"h": "老", "p": "lǎo", "m": "Già, cũ"},
    {"h": "离开", "p": "líkāi", "m": "Rời khỏi"},
    {"h": "礼物", "p": "lǐwù", "m": "Quà tặng"},
    {"h": "历史", "p": "lìshǐ", "m": "Lịch sử"},
    {"h": "脸", "p": "liǎn", "m": "Khuôn mặt"},
    {"h": "练习", "p": "liànxí", "m": "Luyện tập, bài tập"},
    {"h": "辆", "p": "liàng", "m": "Chiếc (xe)"},
    {"h": "聊天(儿)", "p": "liáotiān", "m": "Tán gẫu"},
    {"h": "了解", "p": "liǎojiě", "m": "Hiểu rõ"},
    {"h": "邻居", "p": "línjū", "m": "Hàng xóm"},
    {"h": "留学", "p": "liúxué", "m": "Du học"},
    {"h": "楼", "p": "lóu", "m": "Tòa nhà, lầu"},
    {"h": "绿", "p": "lǜ", "m": "Màu xanh lá cây"},
    {"h": "马", "p": "mǎ", "m": "Con ngựa"},
    {"h": "马上", "p": "mǎshàng", "m": "Liền, ngay lập tức"},
    {"h": "满意", "p": "mǎnyì", "m": "Hài lòng"},
    {"h": "帽子", "p": "màozi", "m": "Cái mũ"},
    {"h": "米", "p": "mǐ", "m": "Mét, gạo"},
    {"h": "面包", "p": "miànbāo", "m": "Bánh mì"},
    {"h": "明白", "p": "míngbai", "m": "Rõ ràng, dễ hiểu"},
    {"h": "拿", "p": "ná", "m": "Cầm, lấy"},
    {"h": "奶奶", "p": "nǎinai", "m": "Bà nội"},
    {"h": "南(方)", "p": "nánfāng", "m": "Phía nam"},
    {"h": "难", "p": "nán", "m": "Khó"},
    {"h": "难过", "p": "nánguò", "m": "Buồn"},
    {"h": "年级", "p": "niánjí", "m": "Lớp (khối)"},
    {"h": "年轻", "p": "niánqīng", "m": "Trẻ tuổi"},
    {"h": "鸟", "p": "niǎo", "m": "Con chim"},
    {"h": "努力", "p": "nǔlì", "m": "Nỗ lực"},
    {"h": "爬山", "p": "páshān", "m": "Leo núi"},
    {"h": "盘子", "p": "pánzi", "m": "Cái đĩa"},
    {"h": "胖", "p": "pàng", "m": "Béo"},
    {"h": "皮鞋", "p": "píxié", "m": "Giày da"},
    {"h": "啤酒", "p": "píjiǔ", "m": "Bia"},
    {"h": "瓶子", "p": "píngzi", "m": "Lọ, bình, chai"},
    {"h": "其实", "p": "qíshí", "m": "Thực ra"},
    {"h": "其他", "p": "qítā", "m": "Cái khác"},
    {"h": "奇怪", "p": "qíguài", "m": "Kỳ lạ"},
    {"h": "骑", "p": "qí", "m": "Cưỡi, đi"},
    {"h": "起飞", "p": "qǐfēi", "m": "Cất cánh"},
    {"h": "起来", "p": "qǐlái", "m": "Lên, đứng dậy"},
    {"h": "清楚", "p": "qīngchu", "m": "Rõ ràng"},
    {"h": "请假", "p": "qǐngjià", "m": "Xin nghỉ phép"},
    {"h": "秋(天)", "p": "qiūtiān", "m": "Mùa thu"},
    {"h": "裙子", "p": "qúnzi", "m": "Cái váy"},
    {"h": "然后", "p": "ránhòu", "m": "Sau đó"},
    {"h": "热情", "p": "rèqíng", "m": "Nhiệt tình"},
    {"h": "认为", "p": "rènwéi", "m": "Cho rằng"},
    {"h": "认真", "p": "rènzhēn", "m": "Nghiêm túc"},
    {"h": "容易", "p": "róngyì", "m": "Dễ"},
    {"h": "如果", "p": "rúguǒ", "m": "Nếu"},
    {"h": "伞", "p": "sǎn", "m": "Ô (dù)"},
    {"h": "上网", "p": "shàngwǎng", "m": "Lên mạng"},
    {"h": "生气", "p": "shēngqì", "m": "Tức giận"},
    {"h": "声音", "p": "shēngyīn", "m": "Âm thanh"},
    {"h": "世界", "p": "shìjiè", "m": "Thế giới"},
    {"h": "试", "p": "shì", "m": "Thử"},
    {"h": "瘦", "p": "shòu", "m": "Gầy, còm"},
    {"h": "叔叔", "p": "shūshu", "m": "Chú"},
    {"h": "舒服", "p": "shūfu", "m": "Dễ chịu"},
    {"h": "树", "p": "shù", "m": "Cây"},
    {"h": "数学", "p": "shùxué", "m": "Môn Toán"},
    {"h": "刷牙", "p": "shuāyá", "m": "Đánh răng"},
    {"h": "双", "p": "shuāng", "m": "Đôi"},
    {"h": "水平", "p": "shuǐpíng", "m": "Trình độ"},
    {"h": "司机", "p": "sījī", "m": "Tài xế"},
    {"h": "太阳", "p": "tàiyáng", "m": "Mặt trời"},
    {"h": "特别", "p": "tèbié", "m": "Vô cùng, đặc biệt"},
    {"h": "疼", "p": "téng", "m": "Đau, nhức"},
    {"h": "提高", "p": "tígāo", "m": "Nâng cao"},
    {"h": "体育", "p": "tǐyù", "m": "Thể dục"},
    {"h": "甜", "p": "tián", "m": "Ngọt"},
    {"h": "条", "p": "tiáo", "m": "Cái (vật dài mỏng)"},
    {"h": "同事", "p": "tóngshì", "m": "Đồng nghiệp"},
    {"h": "同意", "p": "tóngyì", "m": "Đồng ý"},
    {"h": "头发", "p": "tóufa", "m": "Tóc"},
    {"h": "突然", "p": "tūrán", "m": "Bỗng nhiên"},
    {"h": "图书馆", "p": "túshūguǎn", "m": "Thư viện"},
    {"h": "腿", "p": "tuǐ", "m": "Chân"},
    {"h": "完成", "p": "wánchéng", "m": "Hoàn thành"},
    {"h": "碗", "p": "wǎn", "m": "Bát"},
    {"h": "万", "p": "wàn", "m": "Vạn"},
    {"h": "忘记", "p": "wàngjì", "m": "Quên"},
    {"h": "为", "p": "wèi", "m": "Vì, cho"},
    {"h": "为了", "p": "wèile", "m": "Để, vì"},
    {"h": "位", "p": "wèi", "m": "Vị (người)"},
    {"h": "文化", "p": "wénhuà", "m": "Văn hóa"},
    {"h": "西", "p": "xī", "m": "Phía tây"},
    {"h": "习惯", "p": "xíguàn", "m": "Thói quen"},
    {"h": "洗手间", "p": "xǐshǒujiān", "m": "Nhà vệ sinh"},
    {"h": "洗澡", "p": "xǐzǎo", "m": "Tắm"},
    {"h": "夏(天)", "p": "xiàtiān", "m": "Mùa hè"},
    {"h": "先", "p": "xiān", "m": "Trước"},
    {"h": "相信", "p": "xiāngxìn", "m": "Tin tưởng"},
    {"h": "香蕉", "p": "xiāngjiāo", "m": "Chuối"},
    {"h": "向", "p": "xiàng", "m": "Hướng về"},
    {"h": "像", "p": "xiàng", "m": "Giống"},
    {"h": "小心", "p": "xiǎoxīn", "m": "Cẩn thận"},
    {"h": "校长", "p": "xiàozhǎng", "m": "Hiệu trưởng"},
    {"h": "新闻", "p": "xīnwén", "m": "Tin tức"},
    {"h": "新鲜", "p": "xīnxiān", "m": "Tươi mới"},
    {"h": "信用卡", "p": "xìnyòngkǎ", "m": "Thẻ tín dụng"},
    {"h": "行李箱", "p": "xínglǐxiāng", "m": "Vali"},
    {"h": "熊猫", "p": "xióngmāo", "m": "Gấu trúc"},
    {"h": "需要", "p": "xūyào", "m": "Cần"},
    {"h": "选择", "p": "xuǎnzé", "m": "Lựa chọn"},
    {"h": "要求", "p": "yāoqiú", "m": "Yêu cầu"},
    {"h": "爷爷", "p": "yéye", "m": "Ông nội"},
    {"h": "一定", "p": "yídìng", "m": "Nhất định"},
    {"h": "一共", "p": "yígòng", "m": "Tổng cộng"},
    {"h": "一会儿", "p": "yíhuìr", "m": "Một lát"},
    {"h": "一样", "p": "yíyàng", "m": "Giống nhau"},
    {"h": "以前", "p": "yǐqián", "m": "Trước đây"},
    {"h": "一般", "p": "yìbān", "m": "Thông thường"},
    {"h": "一边", "p": "yìbiān", "m": "Vừa... vừa"},
    {"h": "一直", "p": "yìzhí", "m": "Suốt, liên tục"},
    {"h": "音乐", "p": "yīnyuè", "m": "Âm nhạc"},
    {"h": "银行", "p": "yínháng", "m": "Ngân hàng"},
    {"h": "饮料", "p": "yǐnliào", "m": "Đồ uống"},
    {"h": "应该", "p": "yīnggāi", "m": "Nên"},
    {"h": "影响", "p": "yǐngxiǎng", "m": "Ảnh hưởng"},
    {"h": "用", "p": "yòng", "m": "Dùng"},
    {"h": "游戏", "p": "yóuxì", "m": "Trò chơi"},
    {"h": "有名", "p": "yǒumíng", "m": "Nổi tiếng"},
    {"h": "又", "p": "yòu", "m": "Vừa, lại"},
    {"h": "遇到", "p": "yùdào", "m": "Gặp phải"},
    {"h": "元", "p": "yuán", "m": "Đồng (tiền)"},
    {"h": "愿意", "p": "yuànyì", "m": "Muốn, bằng lòng"},
    {"h": "月亮", "p": "yuèliang", "m": "Mặt trăng"},
    {"h": "越", "p": "yuè", "m": "Càng"},
    {"h": "站", "p": "zhàn", "m": "Đứng / Trạm"},
    {"h": "张", "p": "zhāng", "m": "Tờ, tấm (vật phẳng)"},
    {"h": "长", "p": "zhǎng", "m": "Trưởng thành, lớn lên"},
    {"h": "着急", "p": "zháojí", "m": "Lo lắng"},
    {"h": "照顾", "p": "zhàogù", "m": "Chăm sóc"},
    {"h": "照片", "p": "zhàopiàn", "m": "Bức ảnh"},
    {"h": "照相机", "p": "zhàoxiàngjī", "m": "Máy chụp ảnh"},
    {"h": "只(zhī)", "p": "zhī", "m": "Con (động vật)"},
    {"h": "只(zhǐ)", "p": "zhǐ", "m": "Chỉ"},
    {"h": "只有...才", "p": "zhǐyǒu... cái", "m": "Chỉ có... mới..."},
    {"h": "中间", "p": "zhōngjiān", "m": "Giữa"},
    {"h": "终于", "p": "zhōngyú", "m": "Cuối cùng"},
    {"h": "种", "p": "zhǒng", "m": "Loại"},
    {"h": "重要", "p": "zhòngyào", "m": "Quan trọng"},
    {"h": "周末", "p": "zhōumò", "m": "Cuối tuần"},
    {"h": "主要", "p": "zhǔyào", "m": "Chủ yếu"},
    {"h": "注意", "p": "zhùyì", "m": "Chú ý"},
    {"h": "自己", "p": "zìjǐ", "m": "Tự mình"},
    {"h": "自行车", "p": "zìxíngchē", "m": "Xe đạp"},
    {"h": "总是", "p": "zǒngshì", "m": "Luôn luôn"},
    {"h": "嘴", "p": "zuǐ", "m": "Miệng"},
    {"h": "最后", "p": "zuìhòu", "m": "Cuối cùng"},
    {"h": "最近", "p": "zuìjìn", "m": "Gần đây"},
    {"h": "作业", "p": "zuòyè", "m": "Bài tập về nhà"},
    {"h": "黄河", "p": "Huánghé", "m": "Hoàng Hà"}
]

# --- 2. CẤU HÌNH GIAO DIỆN ---
st.set_page_config(page_title="K10 - LUYỆN TẬP 300 TỪ HSK3", page_icon="📝")
st.markdown("<style>header {visibility: hidden;} footer {visibility: hidden;}</style>", unsafe_allow_html=True)

# --- 3. QUẢN LÝ TRẠNG THÁI (SESSION STATE) ---
if 'all_used_words' not in st.session_state:
    st.session_state.all_used_words = []

if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}

if 'result_gif' not in st.session_state:
    st.session_state.result_gif = None

if 'master_questions' not in st.session_state:
    # Lọc bỏ TẤT CẢ các từ đã từng xuất hiện
    available = [v for v in vocab_db if v['h'] not in st.session_state.all_used_words]
    
    # Reset nếu hết kho từ (hoặc còn ít hơn 20 từ)
    if len(available) < 20:
        st.session_state.all_used_words = []
        available = vocab_db
        st.warning("🔄 Đã học hết kho từ! Hệ thống sẽ bắt đầu lại từ đầu.")
        
    sampled = random.sample(available, 20)
    
    for s in sampled:
        st.session_state.all_used_words.append(s['h'])
        
    questions = []
    for item in sampled:
        mode = random.choice(['p', 'm'])
        if mode == 'p':
            q_text = f"Phiên âm của từ '{item['h']}' là gì?"
            correct = item['p']
            others = list(set([v['p'] for v in vocab_db if v['p'] != correct]))
        else:
            q_text = f"Nghĩa của từ '{item['h']}' là gì?"
            correct = item['m']
            others = list(set([v['m'] for v in vocab_db if v['m'] != correct]))
            
        # Lấy 3 đáp án sai ngẫu nhiên
        distractors = random.sample(others, 3)
        options = distractors + [correct]
        random.shuffle(options)
        
        questions.append({
            "q": q_text, 
            "options": options, 
            "a": correct, 
            "word": item['h'],
            "full_info": f"{item['h']} [{item['p']}]: {item['m']}"
        })
        
    st.session_state.master_questions = questions
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.user_answers = {}
    st.session_state.quiz_done = False
    st.session_state.result_gif = None

# --- 4. HIỂN THỊ CÂU HỎI ---
if not st.session_state.quiz_done:
    st.title("🎓 K10 ÔN TẬP 300 TỪ VỰNG HSK3")
    
    total_unique = len(vocab_db)
    st.info(f"Đã luyện tập: {len(set(st.session_state.all_used_words))} / {total_unique} từ. Các câu hỏi sẽ không trùng lại!")
    
    idx = st.session_state.current_idx
    q = st.session_state.master_questions[idx]
    
    st.progress(idx / 20)
    st.subheader(f"Câu {idx+1}/20")
    st.markdown(f"### {q['q']}")
    
    # Giữ lại lựa chọn cũ nếu học viên quay lại câu này
    saved_ans = st.session_state.user_answers.get(idx)
    default_idx = q['options'].index(saved_ans) if saved_ans in q['options'] else 0
        
    choice = st.radio("Chọn đáp án của bạn:", q['options'], index=default_idx, key=f"radio_{idx}")
    
    # Thiết kế 2 cột cho 2 nút Quay lại và Tiếp theo
    col1, col2 = st.columns(2)
    
    with col1:
        if idx > 0:
            if st.button("⬅️ Quay lại câu trước"):
                st.session_state.user_answers[idx] = choice # Lưu tạm đáp án
                st.session_state.current_idx -= 1
                st.rerun()
                
    with col2:
        if idx < 19:
            if st.button("Câu tiếp theo ➡️"):
                st.session_state.user_answers[idx] = choice # Lưu đáp án
                st.session_state.current_idx += 1
                st.rerun()
        else:
            if st.button("Nộp bài 🏁"):
                st.session_state.user_answers[idx] = choice
                
                # Tính điểm toàn bộ bài
                final_score = 0
                for i, mq in enumerate(st.session_state.master_questions):
                    if st.session_state.user_answers.get(i) == mq['a']:
                        final_score += 1
                
                st.session_state.score = final_score
                st.session_state.quiz_done = True
                
                # Random chọn 1 ảnh GIF để hiện chúc mừng
                st.session_state.result_gif = random.choice(gif_urls)
                
                st.rerun()

else:
    st.balloons()
    st.header("HOÀN THÀNH BÀI ÔN TẬP! 🎉")
    
    # Hiện thị chiếc GIF chúc mừng (Blind Box)
    if st.session_state.result_gif:
        st.image(st.session_state.result_gif, width=350)
    
    st.metric("Điểm số của bạn", f"{st.session_state.score}/20")
    
    if st.button("Làm tiếp 20 từ khác (Không trùng từ cũ) 🔄"):
        del st.session_state.master_questions
        del st.session_state.current_idx
        del st.session_state.score
        del st.session_state.user_answers
        del st.session_state.quiz_done
        del st.session_state.result_gif
        st.rerun()

    st.divider()
    st.subheader("Xem lại bài làm lần này:")
    for i, q in enumerate(st.session_state.master_questions):
        user_ans = st.session_state.user_answers.get(i, "Chưa chọn")
        is_correct = user_ans == q['a']
        icon = "✅" if is_correct else "❌"
        
        with st.expander(f"{icon} Câu {i+1}: {q['word']}"):
            st.write(f"**Câu hỏi:** {q['q']}")
            st.write(f"**Bạn chọn:** {user_ans}")
            st.write(f"**Đáp án đúng:** {q['a']}")
            st.info(f"💡 Kiến thức: {q['full_info']}")
