from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# 🔑 NEW TOKEN (from BotFather)
TOKEN = "8616456401:AAG_unU6wElbbV3XI6A7C1OjUhb13ooaYDw"

# =========================
# LINKS (1–5 SYSTEM)
# =========================

APPS = {
    "1": "APP_LINK_1",
    "2": "APP_LINK_2",
    "3": "APP_LINK_3",
    "4": "APP_LINK_4",
    "5": "APP_LINK_5",
}

SITES = {
    "1": "SITE_LINK_1",
    "2": "SITE_LINK_2",
    "3": "SITE_LINK_3",
    "4": "SITE_LINK_4",
    "5": "SITE_LINK_5",
}

SURVEYS = {
    "1": "SURVEY_LINK_1",
    "2": "SURVEY_LINK_2",
    "3": "SURVEY_LINK_3",
    "4": "SURVEY_LINK_4",
    "5": "SURVEY_LINK_5",
}

INSTALL = {
    "1": "INSTALL_LINK_1",
    "2": "INSTALL_LINK_2",
    "3": "INSTALL_LINK_3",
    "4": "INSTALL_LINK_4",
    "5": "INSTALL_LINK_5",
}

# 🔥 CPA / ADSTERRA LINK
TRENDING_LINK = "https://www.effectivecpmnetwork.com/z3q0b6qd?key=b67a254f21a17643073d56dd0745fc9d"

# =========================
# MENU
# =========================
def main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("💰 Earning Apps", callback_data="apps")],
        [InlineKeyboardButton("🌐 Earning Sites", callback_data="sites")],
        [InlineKeyboardButton("🎯 Surveys", callback_data="surveys")],
        [InlineKeyboardButton("📲 Install & Earn", callback_data="install")],
        [InlineKeyboardButton("📊 Trending Offers", callback_data="trending")]
    ])

# =========================
# START
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Reward Hub\n\nChoose a category:",
        reply_markup=main_menu()
    )

# =========================
# BUILD MENU
# =========================
def build_menu(data, title):
    keyboard = [
        [InlineKeyboardButton("1️⃣ Offer 1", url=data["1"])],
        [InlineKeyboardButton("2️⃣ Offer 2", url=data["2"])],
        [InlineKeyboardButton("3️⃣ Offer 3", url=data["3"])],
        [InlineKeyboardButton("4️⃣ Offer 4", url=data["4"])],
        [InlineKeyboardButton("5️⃣ Offer 5", url=data["5"])],
        [InlineKeyboardButton("🔙 Back", callback_data="back")]
    ]
    return title, InlineKeyboardMarkup(keyboard)

# =========================
# CALLBACKS
# =========================
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "apps":
        title, keyboard = build_menu(APPS, "💰 EARNING APPS")
        await query.edit_message_text(title, reply_markup=keyboard)

    elif query.data == "sites":
        title, keyboard = build_menu(SITES, "🌐 EARNING SITES")
        await query.edit_message_text(title, reply_markup=keyboard)

    elif query.data == "surveys":
        title, keyboard = build_menu(SURVEYS, "🎯 SURVEYS")
        await query.edit_message_text(title, reply_markup=keyboard)

    elif query.data == "install":
        title, keyboard = build_menu(INSTALL, "📲 INSTALL & EARN")
        await query.edit_message_text(title, reply_markup=keyboard)

    elif query.data == "trending":
        keyboard = [
            [InlineKeyboardButton("🚀 Start Offer", url=TRENDING_LINK)],
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]
        await query.edit_message_text(
            "📊 TRENDING OFFER 🔥\n\nHigh converting offer available now.",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "back":
        await query.edit_message_text(
            "👋 MAIN MENU",
            reply_markup=main_menu()
        )

# =========================
# RUN
# =========================
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

app.run_polling()
