import uuid
import logging
from datetime import datetime, timedelta, timezone

import bcrypt

logger = logging.getLogger("drizle")

schemes = ["Visa", "Mastercard", "Meeza/Jaywan", "Amex"]
terminals = ["Online E0000003", "Online GP121015", "Online T0000042", "Online M0000018"]
tags_pool = [[], [], ["DCC"], ["DCC"], [], [], ["3DS"], []]
types_pool = ["Purchase", "Refund", "Purchase", "Purchase", "Refund"]
card_classes = ["N/A", "Consumer", "N/A", "Consumer", "N/A"]
card_segments = ["N/A", "Standard", "N/A", "Premium", "N/A"]
card_origins = ["Domestic", "International", "Domestic", "Domestic", "International"]


async def seed(db):
    demo_email = "demo@drizlepay.com"
    onboarding_email = "onboarding@demo.com"

    existing = await db.users.find_one({"email": demo_email})
    if not existing:
        await db.users.insert_one({
            "email": demo_email,
            "password": bcrypt.hashpw("demo123".encode(), bcrypt.gensalt()).decode(),
            "name": "Demo Merchant",
            "company": "Demo SaaS Ltd",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "email_verified": True,
            "active": True,
            "onboarding_status": "approved",
            "onboarding_data": {},
            "kyc_documents": [],
            "api_keys": {
                "publishable": "dp_pub_demo_sample_key",
                "secret": "dp_sec_demo_secret_key_replace_in_prod",
            },
        })

    onboarding_existing = await db.users.find_one({"email": onboarding_email})
    if not onboarding_existing:
        await db.users.insert_one({
            "email": onboarding_email,
            "password": bcrypt.hashpw("demo123".encode(), bcrypt.gensalt()).decode(),
            "name": "Desert Trading LLC",
            "company": "Desert Trading LLC",
            "created_at": datetime.now(timezone.utc).isoformat(),
            "email_verified": True,
            "active": False,
            "onboarding_status": "in_progress",
            "onboarding_data": {
                "business_type": {"type": "llc", "subtype": "ecommerce"},
                "business_details": {
                    "legal_name": "Desert Trading LLC",
                    "trading_name": "Desert Trading",
                    "registration_number": "CR-88492017",
                    "tax_id": "100478963201478",
                    "emirates_id": "784-1992-1234567-1",
                    "website": "https://deserttrading.ae",
                    "phone": "+971552345678",
                    "address": "Office 101, Al Fattan Plaza, Dubai, UAE",
                    "city": "Dubai",
                    "country": "UAE",
                },
                "representative": {
                    "name": "Ahmed Al Mansouri",
                    "email": "ahmed@deserttrading.ae",
                    "phone": "+971552345678",
                    "job_title": "CEO",
                },
                "owners": [
                    {
                        "name": "Ahmed Al Mansouri",
                        "email": "ahmed@deserttrading.ae",
                        "phone": "+971552345678",
                        "nationality": "UAE",
                        "ownership_pct": 100,
                    }
                ],
                "executives": [],
                "products": {
                    "description": "Online retail of electronics and home appliances across the UAE",
                    "industry": "ecommerce",
                    "avg_ticket_size": 450,
                    "expected_monthly_volume": 150000,
                    "target_markets": ["UAE", "Saudi Arabia"],
                },
                "public": {
                    "public_name": "Desert Trading",
                    "support_email": "support@deserttrading.ae",
                    "support_phone": "+971552345678",
                    "support_url": "https://deserttrading.ae/contact",
                    "terms_url": "https://deserttrading.ae/terms",
                    "privacy_url": "https://deserttrading.ae/privacy",
                },
                "bank": {
                    "bank_name": "Emirates NBD",
                    "account_name": "Desert Trading LLC",
                    "account_number": "1012345678",
                    "iban": "AE770260001014273931915",
                    "swift": "EBILAEADXXX",
                },
                "security": {"two_factor_enabled": False},
                "extras": {"referral_source": "Google", "notes": ""},
            },
            "kyc_documents": [
                {
                    "id": "kyc_trade_license",
                    "doc_type": "trade_license",
                    "filename": "trade_license.pdf",
                    "content_type": "application/pdf",
                    "uploaded_at": datetime.now(timezone.utc).isoformat(),
                    "status": "processed",
                },
            ],
            "api_keys": {
                "publishable": "dp_pub_onboarding_sample_key",
                "secret": "dp_sec_onboarding_secret_key_replace_in_prod",
            },
        })

    txn_count = await db.transactions.count_documents({"email": demo_email})
    if txn_count == 0:
        txns = []
        base = datetime.now(timezone.utc) - timedelta(days=31)
        for i in range(85):
            t = base + timedelta(hours=i * 9, minutes=(i * 17) % 60)
            txns.append({
                "email": demo_email,
                "id": f"dp_tx_{i:04d}",
                "reference": f"#bc0ddc4...{uuid.uuid4().hex[:7]}",
                "amount": round(1 + (i * 0.37), 2),
                "currency": "AED" if i % 4 != 0 else "USD",
                "status": "success" if i % 5 != 0 else "refunded",
                "method": ["card", "tabby", "apple_pay", "google_pay", "aani"][i % 5],
                "scheme": schemes[i % len(schemes)],
                "terminal_id": terminals[i % len(terminals)],
                "tags": tags_pool[i % len(tags_pool)],
                "type": types_pool[i % len(types_pool)],
                "card_class": card_classes[i % len(card_classes)],
                "card_segment": card_segments[i % len(card_segments)],
                "card_origin": card_origins[i % len(card_origins)],
                "customer": f"cust_{i:04d}@example.com",
                "created_at": t.isoformat(),
            })
        await db.transactions.insert_many(txns)
        logger.info("Seeded 85 demo transactions")

    payout_count = await db.payouts.count_documents({"email": demo_email})
    if payout_count == 0:
        ps = []
        base_p = datetime.now(timezone.utc) - timedelta(days=30)
        for i in range(12):
            pt = base_p + timedelta(days=i * 2)
            ps.append({
                "email": demo_email,
                "id": f"po_{i:04d}",
                "amount": round(0.5 + (i * 0.3), 2),
                "net_amount": round(0.5 + (i * 0.3), 2),
                "currency": "AED" if i % 3 != 0 else "USD",
                "status": "completed" if i < 9 else "pending",
                "iban": "AE770260001014273931915",
                "tx_count": 1 + (i % 5),
                "period": "June 2026",
                "paid_at": pt.isoformat() if i < 9 else None,
                "created_at": pt.isoformat(),
            })
        await db.payouts.insert_many(ps)
        logger.info("Seeded 12 demo payouts")

    link_count = await db.pay_links.count_documents({"email": demo_email})
    if link_count == 0:
        links = []
        for i in range(8):
            links.append({
                "id": f"dpl_{uuid.uuid4().hex[:12]}",
                "email": demo_email,
                "url": f"https://drizlepay.com/pay/{uuid.uuid4().hex[:16]}",
                "amount": round(10 + (i * 15), 2) if i % 3 != 0 else None,
                "currency": "AED",
                "description": ["Monthly subscription", "Invoice #1423", "Support tier", "Product X", "", "Consulting fee", "Annual plan", ""][i],
                "is_static": i >= 4,
                "is_recurring": i in [0, 6],
                "recurring_interval": "monthly" if i == 0 else "yearly" if i == 6 else None,
                "status": "active" if i < 6 else "disabled",
                "payment_count": i * 3,
                "total_collected": round(i * 45.5, 2),
                "created_at": (datetime.now(timezone.utc) - timedelta(days=i * 4)).isoformat(),
            })
        await db.pay_links.insert_many(links)
        logger.info("Seeded 8 demo pay links")

    team_count = await db.team_members.count_documents({"merchant_email": demo_email})
    if team_count == 0:
        members = [
            {"id": f"tm_{uuid.uuid4().hex[:12]}", "merchant_email": demo_email, "email": "alice@demo.com", "name": "Alice Johnson", "role": "admin", "status": "active", "created_at": (datetime.now(timezone.utc) - timedelta(days=60)).isoformat()},
            {"id": f"tm_{uuid.uuid4().hex[:12]}", "merchant_email": demo_email, "email": "bob@demo.com", "name": "Bob Smith", "role": "developer", "status": "active", "created_at": (datetime.now(timezone.utc) - timedelta(days=30)).isoformat()},
            {"id": f"tm_{uuid.uuid4().hex[:12]}", "merchant_email": demo_email, "email": "carol@demo.com", "name": "Carol Davis", "role": "analyst", "status": "active", "created_at": (datetime.now(timezone.utc) - timedelta(days=14)).isoformat()},
            {"id": f"tm_{uuid.uuid4().hex[:12]}", "merchant_email": demo_email, "email": "invited@demo.com", "name": "", "role": "member", "status": "invited", "created_at": (datetime.now(timezone.utc) - timedelta(days=2)).isoformat()},
        ]
        await db.team_members.insert_many(members)
        logger.info("Seeded 4 demo team members")

    invoice_count = await db.tax_invoices.count_documents({"email": demo_email})
    if invoice_count == 0:
        invoices = []
        for i in range(6):
            invoices.append({
                "email": demo_email,
                "id": f"inv_{i:04d}",
                "period": f"2026-{i+1:02d}",
                "label": f"{['January','February','March','April','May','June'][i]} 2026",
                "amount": round(50 + (i * 12.5), 2),
                "currency": "AED",
                "status": "generated" if i < 4 else "pending",
                "generated_at": (datetime.now(timezone.utc) - timedelta(days=i * 30)).isoformat() if i < 4 else None,
            })
        await db.tax_invoices.insert_many(invoices)
        logger.info("Seeded 6 demo tax invoices")

    stmt_count = await db.monthly_statements.count_documents({"email": demo_email})
    if stmt_count == 0:
        stmts = []
        for i in range(6):
            stmts.append({
                "email": demo_email,
                "id": f"stmt_{i:04d}",
                "period": f"2026-{i+1:02d}",
                "label": f"{['January','February','March','April','May','June'][i]} 2026",
                "total_volume": round(500 + (i * 150), 2),
                "total_fees": round(15 + (i * 4.5), 2),
                "net_amount": round(485 + (i * 145.5), 2),
                "currency": "AED",
                "status": "generated" if i < 4 else "pending",
                "generated_at": (datetime.now(timezone.utc) - timedelta(days=i * 30)).isoformat() if i < 4 else None,
            })
        await db.monthly_statements.insert_many(stmts)
        logger.info("Seeded 6 demo monthly statements")

    ticket_count = await db.support_tickets.count_documents({"email": demo_email})
    if ticket_count == 0:
        tickets = [
            {
                "_id": f"st_{uuid.uuid4().hex[:12]}",
                "email": demo_email,
                "subject": "Payment settlement delay",
                "category": "Payments",
                "message": "One of my transactions from yesterday hasn't settled yet. The status shows 'processing' for more than 24 hours.",
                "priority": "high",
                "status": "open",
                "created_at": (datetime.now(timezone.utc) - timedelta(hours=6)).isoformat(),
            },
            {
                "_id": f"st_{uuid.uuid4().hex[:12]}",
                "email": demo_email,
                "subject": "API key rotation request",
                "category": "API",
                "message": "I need to rotate my API keys for security purposes. Can you help with that?",
                "priority": "normal",
                "status": "open",
                "created_at": (datetime.now(timezone.utc) - timedelta(days=2)).isoformat(),
            },
            {
                "_id": f"st_{uuid.uuid4().hex[:12]}",
                "email": demo_email,
                "subject": "Refund not showing in dashboard",
                "category": "Payments",
                "message": "I processed a refund but it's not appearing in my transaction history. The refund ID is dp_rx_abc123.",
                "priority": "normal",
                "status": "resolved",
                "created_at": (datetime.now(timezone.utc) - timedelta(days=5)).isoformat(),
            },
        ]
        await db.support_tickets.insert_many(tickets)
        logger.info("Seeded 3 demo support tickets")
