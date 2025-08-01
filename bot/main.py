from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from server import get_balance, fund_wallet, withdraw, get_transactions
from decouple import config

BOT_TOKEN = config("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to WalletBot!\n Your one stop bot for all payments. Kindly use the commands below to carry out any transaction of your choice\n\nUse /balance,\n /fund <amount>,\n /withdraw <amount>,\n /transactions"
    )

# Handle Balance
async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    print(update.effective_user.username, update.effective_user.full_name)
    bal = get_balance(user_id)
    await update.message.reply_text(f"Your wallet balance is ${bal:.2f}")

# Handle Funding
async def fund(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    print(update.effective_user.username, update.effective_user.full_name)
    try:
        amount = float(context.args[0])
        fund_wallet(user_id, amount)
        new_bal = get_balance(user_id)
        await update.message.reply_text(
            f"Wallet funded with ${amount:.2f}. New balance: ${new_bal:.2f}"
        )
    except (IndexError, ValueError):
        await update.message.reply_text("Usage: /fund <amount>")

# Handle Withdrawal
async def withdraw_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    try:
        amount = float(context.args[0])
        if withdraw(user_id, amount):
            new_bal = get_balance(user_id)
            await update.message.reply_text(
                f"Withdrew ${amount:.2f}. New balance: ${new_bal:.2f}"
            )
        else:
            await update.message.reply_text("Insufficient funds")
    except (IndexError, ValueError):
        await update.message.reply_text("Usage: /withdraw <amount>")

# Handle Transaction
async def transactions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    txs = get_transactions(user_id)
    if not txs:
        await update.message.reply_text("You have not made any transactions yet")
    else:
        msg = "\n".join(
            f"{tx['type'].capitalize()} ${tx['amount']:.2f} at {tx['time']}" for tx in txs
        )
        await update.message.reply_text(msg)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("balance", balance))
app.add_handler(CommandHandler("fund", fund))
app.add_handler(CommandHandler("withdraw", withdraw_cmd))
app.add_handler(CommandHandler("transactions", transactions))

if __name__ == "__main__":
    app.run_polling()
