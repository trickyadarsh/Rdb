from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="𝑷𝒂𝒖𝒔𝒆",
            description=f"𝑷𝒂𝒖𝒔𝒆 𝑻𝒉𝒆 𝑪𝒖𝒓𝒓𝒆𝒏𝒕 𝑷𝒍𝒂𝒚𝒊𝒏𝒈 𝑺𝒕𝒂𝒓𝒆𝒎 𝑶𝒏 𝑽𝒊𝒅𝒆𝒐𝒄𝒉𝒂𝒕  𝑾𝒚𝒏𝒌 𝑴𝒖𝒔𝒊𝒄.",
            thumb_url="https://images.hindustantimes.com/tech/rf/image_size_960x540/HT/p2/2019/11/28/Pictures/_467b713e-11d7-11ea-b3fe-5324eb805ee9.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="𝑹𝒆𝒔𝒖𝒎𝒆",
            description=f"𝑹𝒆𝒔𝒖𝒎𝒆 𝑻𝒉𝒆 𝑪𝒖𝒓𝒓𝒆𝒏𝒕 𝑷𝒍𝒂𝒚𝒊𝒏𝒈 𝑺𝒕𝒂𝒓𝒆𝒎 𝑶𝒏 𝑽𝒊𝒅𝒆𝒐𝒄𝒉𝒂𝒕  𝑾𝒚𝒏𝒌 𝑴𝒖𝒔𝒊𝒄.",
            thumb_url="https://images.hindustantimes.com/tech/rf/image_size_960x540/HT/p2/2019/11/28/Pictures/_467b713e-11d7-11ea-b3fe-5324eb805ee9.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="𝑺𝒌𝒊𝒑",
            description=f"𝑺𝒌𝒊𝒑 𝑻𝒉𝒆 𝑪𝒖𝒓𝒓𝒆𝒏𝒕 𝑷𝒍𝒂𝒚𝒊𝒏𝒈 𝑺𝒕𝒂𝒓𝒆𝒎 𝑶𝒏 𝑽𝒊𝒅𝒆𝒐𝒄𝒉𝒂𝒕  𝑾𝒚𝒏𝒌 𝑴𝒖𝒔𝒊𝒄 .",
            thumb_url="https://images.hindustantimes.com/tech/rf/image_size_960x540/HT/p2/2019/11/28/Pictures/_467b713e-11d7-11ea-b3fe-5324eb805ee9.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="𝑬𝒏𝒅",
            description="𝑬𝒏𝒅 𝑻𝒉𝒆 𝑪𝒖𝒓𝒓𝒆𝒏𝒕 𝑷𝒍𝒂𝒚𝒊𝒏𝒈 𝑺𝒕𝒂𝒓𝒆𝒎 𝑶𝒏 𝑽𝒊𝒅𝒆𝒐𝒄𝒉𝒂𝒕  𝑾𝒚𝒏𝒌 𝑴𝒖𝒔𝒊𝒄.",
            thumb_url="https://images.hindustantimes.com/tech/rf/image_size_960x540/HT/p2/2019/11/28/Pictures/_467b713e-11d7-11ea-b3fe-5324eb805ee9.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="𝑺𝒉𝒖𝒇𝒇𝒍𝒆",
            description="𝑺𝒉𝒖𝒇𝒇𝒍𝒆 𝑻𝒉𝒆 𝑸𝒖𝒆𝒖𝒆𝒅 𝑺𝒐𝒏𝒈 𝑰𝒏 𝑷𝒍𝒂𝒚𝒍𝒊𝒔𝒕",
            thumb_url="https://images.hindustantimes.com/tech/rf/image_size_960x540/HT/p2/2019/11/28/Pictures/_467b713e-11d7-11ea-b3fe-5324eb805ee9.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="𝑳𝒐𝒐𝒑",
            description="𝑳𝒐𝒐𝒑 𝑻𝒉𝒆 𝑪𝒖𝒓𝒓𝒆𝒏𝒕 𝑷𝒍𝒂𝒚𝒊𝒏𝒈 𝑺𝒕𝒂𝒓𝒆𝒎 𝑶𝒏 𝑽𝒊𝒅𝒆𝒐𝒄𝒉𝒂𝒕  𝑾𝒚𝒏𝒌 𝑴𝒖𝒔𝒊𝒄.",
            thumb_url="https://images.hindustantimes.com/tech/rf/image_size_960x540/HT/p2/2019/11/28/Pictures/_467b713e-11d7-11ea-b3fe-5324eb805ee9.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
