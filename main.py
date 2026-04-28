from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.exceptions import TelegramBadRequest
import asyncio
import os
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

# Извлекаем токен
TOKEN = os.getenv("BOT_TOKEN")


bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

# ---------------- ЭМОДЗИ ----------------
EMOJI = {
    "Фрукты": "🍎",
    "Овощи": "🥕",
    "Мясо": "🥩",
    "Рыба и морепродукты": "🐟",
    "Молочные продукты": "🥛",
    "Крупы": "🌾",
    "Назад": "⬅️",
    "Категории": "📄",
    "Банан": "🍌",
    "Апельсин": "🍊",
    "Мандарин": "🍊",
    "Груша": "🍐",
    "Виноград": "🍇",
    "Киви": "🥝",
    "Картофель": "🥔",
    "Морковь": "🥕",
    "Лук": "🧅",
    "Чеснок": "🧄",
    "Помидор": "🍅",
    "Огурец": "🥒",
    "Капуста": "🥬",
    "Брокколи": "🥦",
    "Перец": "🫑",
    "Говядина": "🥩",
    "Курица": "🍗",
    "Индейка": "🦃",
    "Баранина": "🍖",
    "Утка": "🦆",
    "Лосось": "🐟",
    "Тунец": "🐟",
    "Скумбрия": "🐟",
    "Креветки": "🦐",
    "Молоко": "🥛",
    "Кефир": "🥛",
    "Йогурт": "🥣",
    "Сыр": "🧀",
    "Творог": "🍮",
    "Сметана": "🥄",
    "Рис": "🍚",
    "Гречка": "🥣",
    "Овсянка": "🥣",
    "Кукуруза": "🌽",
}

# ---------------- КЛАВИАТУРЫ ----------------

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f"{EMOJI['Категории']} Категории")]
    ],
    resize_keyboard=True
)

categories_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text=f"{EMOJI['Фрукты']} Фрукты")],
        [KeyboardButton(text=f"{EMOJI['Овощи']} Овощи")],
        [KeyboardButton(text=f"{EMOJI['Мясо']} Мясо")],
        [KeyboardButton(text=f"{EMOJI['Рыба и морепродукты']} Рыба и морепродукты")],
        [KeyboardButton(text=f"{EMOJI['Молочные продукты']} Молочные продукты")],
        [KeyboardButton(text=f"{EMOJI['Крупы']} Крупы")],
        [KeyboardButton(text=f"{EMOJI['Назад']} Назад")]
    ],
    resize_keyboard=True
)

# ---------------- ФОТОГРАФИИ ПРОДУКТОВ (проверенные URL) ----------------

PRODUCT_IMAGES = {
    "Банан": "https://upload.wikimedia.org/wikipedia/commons/8/8a/Banana-Single.jpg",
    "Апельсин": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Orange-Fruit-Pieces.jpg",
    "Мандарин": "https://upload.wikimedia.org/wikipedia/commons/4/49/Mandarin_Oranges_%28Citrus_Reticulata%29.jpg",
    "Груша": "https://upload.wikimedia.org/wikipedia/commons/c/cf/Pears.jpg",
    "Виноград": "https://upload.wikimedia.org/wikipedia/commons/b/bb/Table_grapes_on_white.jpg",
    "Киви": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Kiwifruit-Actinidia_deliciosa_sliced.jpg/800px-Kiwifruit-Actinidia_deliciosa_sliced.jpg",
    "Картофель": "https://upload.wikimedia.org/wikipedia/commons/a/ab/Patates.jpg",
    "Морковь": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Carrots.JPG/800px-Carrots.JPG",
    "Лук": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a6/Onion_on_White.JPG/800px-Onion_on_White.JPG",
    "Чеснок": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Garlic_bulb.jpg/800px-Garlic_bulb.jpg",
    "Помидор": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Tomato_je.jpg/800px-Tomato_je.jpg",
    "Огурец": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/Cucumber_cross_section.jpg/800px-Cucumber_cross_section.jpg",
    "Капуста": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Cabbage_and_cross_section_on_white.jpg/800px-Cabbage_and_cross_section_on_white.jpg",
    "Брокколи": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Broccoli_and_cross_section_edit.jpg/800px-Broccoli_and_cross_section_edit.jpg",
    "Перец": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Green-Yellow-Red-Pepper-2009.jpg/800px-Green-Yellow-Red-Pepper-2009.jpg",
    "Говядина": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/Raw_beef_steak.jpg/800px-Raw_beef_steak.jpg",
    "Курица": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Roast_chicken.jpg/800px-Roast_chicken.jpg",
    "Индейка": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Roast_Turkey.jpg/800px-Roast_Turkey.jpg",
    "Баранина": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Lamb_chops.jpg/800px-Lamb_chops.jpg",
    "Утка": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Roast_Duck.jpg/800px-Roast_Duck.jpg",
    "Лосось": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/Salmon_sushi.jpg/800px-Salmon_sushi.jpg",
    "Тунец": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Tuna_fish.jpg/800px-Tuna_fish.jpg",
    "Скумбрия": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Mackerel.jpg/800px-Mackerel.jpg",
    "Креветки": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Shrimp_01.jpg/800px-Shrimp_01.jpg",
    "Молоко": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0e/Milk_glass.jpg/800px-Milk_glass.jpg",
    "Кефир": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/83/Kefir_in_a_glass.JPG/800px-Kefir_in_a_glass.JPG",
    "Йогурт": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Yogurt.jpg/800px-Yogurt.jpg",
    "Сыр": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Cheese_platter.jpg/800px-Cheese_platter.jpg",
    "Творог": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Cottage_cheese.jpg/800px-Cottage_cheese.jpg",
    "Сметана": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Sour_cream.jpg/800px-Sour_cream.jpg",
    "Рис": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Rice_paddy.jpg/800px-Rice_paddy.jpg",
    "Гречка": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Buckwheat_grain.jpg/800px-Buckwheat_grain.jpg",
    "Овсянка": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Oatmeal.jpg/800px-Oatmeal.jpg",
    "Кукуруза": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Corn_on_the_cob.jpg/800px-Corn_on_the_cob.jpg",
}

# ---------------- ДАННЫЕ ----------------

PRODUCTS = {
    "Фрукты": {
        "Банан": {
            "Калории": "89 ккал",
            "Витамины": "B6, C",
            "Польза": "даёт энергию, полезен для сердца",
            "Факт": "содержит калий",
            "Химсостав": "калий, магний"
        },
        "Апельсин": {
            "Калории": "47 ккал",
            "Витамины": "C, B9, B1",
            "Польза": "укрепляет иммунитет",
            "Факт": "покрывает суточную норму витамина C",
            "Химсостав": "кальций, калий"
        },
        "Мандарин": {
            "Калории": "53 ккал",
            "Витамины": "C, A, B1",
            "Польза": "улучшает обмен веществ",
            "Факт": "легко усваивается организмом",
            "Химсостав": "калий, магний"
        },
        "Груша": {
            "Калории": "57 ккал",
            "Витамины": "C, K, E",
            "Польза": "полезна для пищеварения",
            "Факт": "содержит много клетчатки",
            "Химсостав": "калий, медь"
        },
        "Виноград": {
            "Калории": "70 ккал",
            "Витамины": "C, K, B6",
            "Польза": "улучшает работу сердца",
            "Факт": "содержит антиоксиданты",
            "Химсостав": "калий, марганец"
        },
        "Киви": {
            "Калории": "61 ккал",
            "Витамины": "C, E, K",
            "Польза": "укрепляет иммунитет",
            "Факт": "больше витамина C, чем в апельсине",
            "Химсостав": "калий, медь"
        }
    },

    "Овощи": {
        "Картофель": {
            "Калории": "80 ккал",
            "Витамины": "C, B6, B2",
            "Польза": "даёт энергию",
            "Факт": "содержит крахмал",
            "Химсостав": "калий, фосфор"
        },
        "Морковь": {
            "Калории": "41 ккал",
            "Витамины": "A, K, B6",
            "Польза": "улучшает зрение",
            "Факт": "богата бета-каротином",
            "Химсостав": "калий, магний"
        },
        "Лук": {
            "Калории": "40 ккал",
            "Витамины": "C, B6, B9",
            "Польза": "укрепляет иммунитет",
            "Факт": "содержит много сахара",
            "Химсостав": "калий, сера"
        },
        "Чеснок": {
            "Калории": "149 ккал",
            "Витамины": "B6, C, B1",
            "Польза": "борется с бактериями",
            "Факт": "усиливает иммунитет",
            "Химсостав": "сера, кальций"
        },
        "Помидор": {
            "Калории": "20 ккал",
            "Витамины": "C, K, A",
            "Польза": "полезен для сердца",
            "Факт": "содержит ликопин",
            "Химсостав": "калий, магний"
        },
        "Огурец": {
            "Калории": "15 ккал",
            "Витамины": "K, C, B1",
            "Польза": "увлажняет организм",
            "Факт": "95% воды",
            "Химсостав": "калий, кремний"
        },
        "Капуста": {
            "Калории": "28 ккал",
            "Витамины": "C, K, B1",
            "Польза": "улучшает пищеварение",
            "Факт": "полезна для кишечника",
            "Химсостав": "кальций, калий"
        },
        "Брокколи": {
            "Калории": "34 ккал",
            "Витамины": "C, K, A",
            "Польза": "укрепляет иммунитет",
            "Факт": "один из самых полезных овощей",
            "Химсостав": "кальций, железо"
        },
        "Перец": {
            "Калории": "30 ккал",
            "Витамины": "C, A, B6",
            "Польза": "улучшает иммунитет",
            "Факт": "больше витамина C, чем лимон",
            "Химсостав": "калий, магний"
        }
    },

    "Мясо": {
        "Говядина": {
            "Калории": "220 ккал",
            "Витамины": "B12, B1, B2",
            "Польза": "укрепляет мышцы",
            "Факт": "источник железа",
            "Химсостав": "железо, цинк"
        },
        "Курица": {
            "Калории": "150 ккал",
            "Витамины": "B6, B3, B5",
            "Польза": "легко усваивается",
            "Факт": "диетическое мясо",
            "Химсостав": "фосфор, калий"
        },
        "Индейка": {
            "Калории": "180 ккал",
            "Витамины": "B6, B12, B3",
            "Польза": "полезна для мышц",
            "Факт": "мало жира",
            "Химсостав": "железо, цинк"
        },
        "Баранина": {
            "Калории": "290 ккал",
            "Витамины": "B12, B3, E",
            "Польза": "защищает зубы",
            "Факт": "богата белком",
            "Химсостав": "фтор, железо"
        },
        "Утка": {
            "Калории": "300 ккал",
            "Витамины": "B6, B5, A",
            "Польза": "улучшает обмен веществ",
            "Факт": "жирное мясо",
            "Химсостав": "железо, фосфор"
        }
    },

    "Рыба и морепродукты": {
        "Лосось": {
            "Калории": "208 ккал",
            "Витамины": "D, B12, B6",
            "Польза": "богат омега‑3",
            "Факт": "очень питательная рыба",
            "Химсостав": "омега‑3, йод"
        },
        "Тунец": {
            "Калории": "132 ккал",
            "Витамины": "B3, B6, B12",
            "Польза": "много белка",
            "Факт": "часто в спортивном питании",
            "Химсостав": "фосфор, селен"
        },
        "Скумбрия": {
            "Калории": "205 ккал",
            "Витамины": "D, B12",
            "Польза": "полезна для сердца",
            "Факт": "очень питательная",
            "Химсостав": "омега‑3, йод"
        },
        "Креветки": {
            "Калории": "99 ккал",
            "Витамины": "B12, E",
            "Польза": "много белка",
            "Факт": "богаты йодом",
            "Химсостав": "йод, цинк"
        }
    },

    "Молочные продукты": {
        "Молоко": {
            "Калории": "60 ккал",
            "Витамины": "B2, B12, D",
            "Польза": "укрепляет кости",
            "Факт": "источник кальция",
            "Химсостав": "кальций, фосфор"
        },
        "Кефир": {
            "Калории": "50–60 ккал",
            "Витамины": "B2, B12",
            "Польза": "улучшает пищеварение",
            "Факт": "содержит пробиотики",
            "Химсостав": "кальций, магний"
        },
        "Йогурт": {
            "Калории": "60–80 ккал",
            "Витамины": "B2, B12",
            "Польза": "поддерживает микрофлору",
            "Факт": "живые бактерии",
            "Химсостав": "кальций, фосфор"
        },
        "Сыр": {
            "Калории": "250–350 ккал",
            "Витамины": "A, B12",
            "Польза": "богат белком",
            "Факт": "твёрдые сыры калорийные",
            "Химсостав": "кальций, натрий"
        },
        "Творог": {
            "Калории": "120–170 ккал",
            "Витамины": "B2, B12",
            "Польза": "источник белка",
            "Факт": "часто в спорте",
            "Химсостав": "кальций, фосфор"
        },
        "Сметана": {
            "Калории": "180–250 ккал",
            "Витамины": "A, E",
            "Польза": "содержит полезные жиры",
            "Факт": "густой вкус",
            "Химсостав": "кальций, калий"
        }
    },

    "Крупы": {
        "Рис": {
            "Калории": "130 ккал",
            "Витамины": "B1, B3",
            "Польза": "лёгкий источник энергии",
            "Факт": "белый рис усваивается быстрее",
            "Химсостав": "магний, фосфор"
        },
        "Гречка": {
            "Калории": "110–120 ккал",
            "Витамины": "B1, B2",
            "Польза": "богата железом",
            "Факт": "не содержит глютен",
            "Химсостав": "железо, магний"
        },
        "Овсянка": {
            "Калории": "350 ккал",
            "Витамины": "B1, B5",
            "Польза": "снижает холестерин",
            "Факт": "содержит бета‑глюканы",
            "Химсостав": "магний, фосфор"
        },
        "Кукуруза": {
            "Калории": "86 ккал",
            "Витамины": "B1, C",
            "Польза": "антиоксиданты",
            "Факт": "древнейшая культура",
            "Химсостав": "магний, калий"
        }
    }
}


# ---------------- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ----------------

def get_category_by_product(product_name: str) -> str | None:
    """Находит категорию по названию продукта."""
    for category, items in PRODUCTS.items():
        if product_name in items:
            return category
    return None


def build_products_keyboard(category: str) -> ReplyKeyboardMarkup:
    """Создаёт Reply-клавиатуру с продуктами категории."""
    buttons = []
    for product in PRODUCTS[category].keys():
        emoji = EMOJI.get(product, "🍽️")
        buttons.append([KeyboardButton(text=f"{emoji} {product}")])
    buttons.append([KeyboardButton(text=f"{EMOJI['Назад']} Назад")])
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


# ---------------- ХЕНДЛЕРЫ ----------------

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "👋 Добро пожаловать в бот полезных продуктов!\n\n"
        "Выберите категорию, чтобы узнать больше о продуктах питания.",
        reply_markup=main_kb
    )


@dp.message(lambda msg: msg.text == f"{EMOJI['Категории']} Категории")
async def show_categories(message: types.Message):
    await message.answer(
        "📂 Выберите категорию продуктов:",
        reply_markup=categories_kb
    )


@dp.message(lambda msg: msg.text == f"{EMOJI['Назад']} Назад")
async def back_to_main(message: types.Message):
    await message.answer(
        "🔙 Главное меню:",
        reply_markup=main_kb
    )


@dp.message(lambda msg: any(msg.text == f"{EMOJI.get(cat, '')} {cat}" for cat in PRODUCTS.keys()))
async def show_items(message: types.Message):
    # Извлекаем название категории (убираем эмодзи)
    text = message.text
    category = None
    for cat in PRODUCTS.keys():
        if text.endswith(cat):
            category = cat
            break

    if category and category in PRODUCTS:
        items = list(PRODUCTS[category].keys())
        text = f"<b>{EMOJI.get(category, '')} {category}</b>\n\nВыберите продукт:"
        await message.answer(text, reply_markup=build_products_keyboard(category))


@dp.message()
async def show_product_info(message: types.Message):
    # Извлекаем название продукта (убираем эмодзи)
    product_name = None
    for category, items in PRODUCTS.items():
        for item in items.keys():
            if message.text.endswith(item):
                product_name = item
                break
        if product_name:
            break

    if not product_name:
        return

    category = get_category_by_product(product_name)
    data = PRODUCTS[category][product_name]
    image_url = PRODUCT_IMAGES.get(product_name)

    caption = (
        f"<b>{EMOJI.get(product_name, '🍽️')} {product_name}</b>\n\n"
        f"🔥 <b>Калории:</b> {data['Калории']}\n"
        f"💊 <b>Витамины:</b> {data['Витамины']}\n"
        f"✨ <b>Польза:</b> {data['Польза']}\n"
        f"💡 <b>Интересный факт:</b> {data['Факт']}\n"
        f"🧪 <b>Химический состав:</b> {data['Химсостав']}"
    )

    if image_url:
        try:
            await message.answer_photo(
                photo=image_url,
                caption=caption,
                reply_markup=build_products_keyboard(category)
            )
        except TelegramBadRequest:
            # Если фото не загрузилось — отправляем только текст
            await message.answer(
                caption,
                reply_markup=build_products_keyboard(category)
            )
    else:
        await message.answer(
            caption,
            reply_markup=build_products_keyboard(category)
        )


# ---------------- ЗАПУСК ----------------

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())