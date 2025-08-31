# Simple Bill Reminder System - Project Scaffold

## Architecture: Serverless SMS Service with Simple Web Interface

## Technology Stack: Node.js with Twilio SMS, Cron Scheduling, and Local Storage

## Directory Structure

```
simple-bill-reminder/
├── src/
│   ├── components/
│   │   ├── BillEntry.js              // Simple bill setup form (name, date, frequency)
│   │   ├── BillList.js               // Display and mark bills as paid
│   │   └── PaymentConfirm.js         // One-click payment confirmation
│   ├── services/
│   │   ├── SmsService.js             // Twilio SMS reminder sending
│   │   ├── SchedulerService.js       // Cron-based reminder scheduling
│   │   └── StorageService.js         // Local storage for bill data
│   ├── utils/
│   │   ├── DateCalculator.js         // Calculate reminder timing
│   │   └── MessageFormatter.js       // Format SMS reminder text
│   └── data/
│       └── bills.json                // Simple JSON storage for bills
├── functions/
│   └── sendReminders.js              // Serverless function for SMS sending
├── package.json
├── .env.example                      // Twilio credentials template
└── README.md
```

## Key Implementation Files

### src/services/SmsService.js

```javascript
/**
 * Twilio SMS service for sending bill reminders
 * Handles simple text notifications without spam
 */
const twilio = require('twilio');

class SmsService {
  constructor() {
    this.client = twilio(process.env.TWILIO_SID, process.env.TWILIO_TOKEN);
  }

  /**
   * Send simple reminder text
   * Format: "Your [bill name] is due in [X] days"
   */
  async sendReminder(phoneNumber, billName, daysUntilDue) {
    const message = `Your ${billName} is due in ${daysUntilDue} days`;

    try {
      await this.client.messages.create({
        body: message,
        from: process.env.TWILIO_PHONE,
        to: phoneNumber,
      });
      // TODO: Log successful send, mark reminder as sent
    } catch (error) {
      // TODO: Handle SMS failures gracefully
      console.error('SMS send failed:', error);
    }
  }
}

export default SmsService;
```

### src/components/BillEntry.js

```javascript
import React, { useState } from 'react';

/**
 * Simple bill entry form - must not feel like a chore
 * Only essential fields: name, due date, how often
 */
export default function BillEntry() {
  const [billData, setBillData] = useState({
    name: '', // Bill name (e.g., "Electric bill")
    dueDate: '', // Due date each month
    frequency: 'monthly', // Default to monthly
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    // TODO: Save to local storage
    // TODO: Set up reminder schedule
    // TODO: Clear form for next bill
  };

  return (
    <form
      onSubmit={handleSubmit}
      style={{ maxWidth: '300px', margin: '20px auto' }}
    >
      <div>
        <label>Bill Name:</label>
        <input
          type="text"
          value={billData.name}
          onChange={(e) => setBillData({ ...billData, name: e.target.value })}
          placeholder="e.g., Electric bill"
          required
        />
      </div>

      <div>
        <label>Due Date:</label>
        <input
          type="number"
          min="1"
          max="31"
          value={billData.dueDate}
          onChange={(e) =>
            setBillData({ ...billData, dueDate: e.target.value })
          }
          placeholder="Day of month (e.g., 15)"
          required
        />
      </div>

      <button type="submit">Add Bill</button>
      {/* TODO: Keep interface minimal - no overwhelming options */}
    </form>
  );
}
```

### src/services/SchedulerService.js

```javascript
/**
 * Handles reminder scheduling without overwhelming user
 * Sends reminders 3 days before due date (not too many, not too few)
 */
const cron = require('node-cron');

class SchedulerService {
  constructor(smsService, storageService) {
    this.smsService = smsService;
    this.storageService = storageService;
  }

  /**
   * Set up daily check for bills due in 3 days
   * Runs once per day to avoid spam
   */
  startDailyCheck() {
    // Run at 9 AM every day
    cron.schedule('0 9 * * *', () => {
      this.checkUpcomingBills();
    });
  }

  /**
   * Check for bills due in 3 days and send reminders
   * Only send one reminder per bill to avoid spam
   */
  async checkUpcomingBills() {
    const bills = await this.storageService.getUnpaidBills();
    const today = new Date();

    bills.forEach((bill) => {
      const dueDate = this.calculateNextDueDate(bill);
      const daysUntil = Math.ceil((dueDate - today) / (1000 * 60 * 60 * 24));

      // Send reminder 3 days before due date
      if (daysUntil === 3 && !bill.reminderSent) {
        this.smsService.sendReminder(
          process.env.USER_PHONE,
          bill.name,
          daysUntil
        );
        // TODO: Mark reminder as sent to prevent spam
        this.storageService.markReminderSent(bill.id);
      }
    });
  }

  /**
   * Calculate next due date for recurring bill
   */
  calculateNextDueDate(bill) {
    // TODO: Handle monthly recurring bills
    // TODO: Account for different month lengths
  }
}

export default SchedulerService;
```

### src/components/PaymentConfirm.js

```javascript
import React from 'react';

/**
 * Simple one-click payment confirmation
 * Stops reminders immediately when marked as paid
 */
export default function PaymentConfirm({ bill, onMarkPaid }) {
  const handleMarkPaid = () => {
    // TODO: Update bill status to paid
    // TODO: Stop any pending reminders
    // TODO: Reset for next month
    onMarkPaid(bill.id);
  };

  return (
    <div style={{ padding: '10px', border: '1px solid #ccc', margin: '5px' }}>
      <span>
        {bill.name} - Due: {bill.dueDate}
      </span>
      <button
        onClick={handleMarkPaid}
        style={{
          marginLeft: '10px',
          backgroundColor: '#4CAF50',
          color: 'white',
        }}
      >
        Mark as Paid
      </button>
      {/* TODO: Provide immediate visual feedback */}
      {/* TODO: No nagging after marked as paid */}
    </div>
  );
}
```

### functions/sendReminders.js

```javascript
/**
 * Serverless function for reliable SMS sending
 * Ensures reminders work even when computer is off
 */
const SmsService = require('../src/services/SmsService');
const StorageService = require('../src/services/StorageService');

exports.handler = async (event, context) => {
  const smsService = new SmsService();
  const storageService = new StorageService();

  try {
    // TODO: Check for bills due in 3 days
    // TODO: Send SMS reminders
    // TODO: Update reminder status

    return {
      statusCode: 200,
      body: JSON.stringify({ message: 'Reminders sent successfully' }),
    };
  } catch (error) {
    // TODO: Handle failures gracefully - never miss a reminder
    console.error('Reminder function failed:', error);
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Reminder sending failed' }),
    };
  }
};
```

## Technology Stack Details

- **Node.js**: Simple server-side JavaScript
- **Twilio SMS**: Reliable text message delivery
- **React**: Minimal web interface for setup and confirmation
- **Cron**: Scheduled reminder checking
- **Local JSON Storage**: No database complexity, no accounts needed
- **Serverless Functions**: Reliable operation without maintaining servers

## Key Design Principles

1. **No Account Required**: Store data locally, no sign-up process
2. **Minimal Setup**: Only 3 fields per bill (name, due date, frequency)
3. **Reliable Reminders**: 3-day advance notice, one reminder per bill
4. **Immediate Confirmation**: One-click "mark as paid" stops all reminders
5. **No Spam**: Single reminder per bill, stops when marked paid
6. **Works While Traveling**: SMS works anywhere with cell service

## Acceptance Criteria Implementation

1. **No Late Fees**: 3-day advance SMS reminders ensure time to pay
2. **Simple Setup**: Minimal 3-field form, no overwhelming options
3. **Reliable Operation**: Serverless functions ensure reminders never fail
4. **No Spam**: One reminder per bill, immediate stop when marked paid
5. **No Account Complexity**: Local storage, no ads, no login required

This scaffold implements a serverless SMS-based architecture focused on simplicity and reliability for preventing late fees.
