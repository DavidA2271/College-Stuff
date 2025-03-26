using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System.ComponentModel;
using System.Globalization;

namespace Easy_Planning_Calendar
{
    public class CustomMonthObject : Panel
    {
        DateTime currentDate = new DateTime(DateTime.Today.Year, DateTime.Today.Month, 1);
        public DateTime CurrentDate { get => currentDate;
            set { currentDate = value; DateChanged(); } }
        
        CustomMonthCalendarHeader TitlePanel;
        CustomMonthGrid MonthTable;

        public CustomMonthObject()
        {
            JSONHelper.Init();

            Dock = DockStyle.Fill;

            TitlePanel = new CustomMonthCalendarHeader(CurrentDate.Month - 1, CurrentDate.Year);
            MonthTable = new CustomMonthGrid(CurrentDate);

            SizeChanged += AutosizeControl;
            // Need to do it like this so setter activates.
            TitlePanel.MonthChanged += ChangeMonth;

            // Month table needs to go first because of Dock.Fill
            Controls.Add(MonthTable);
            Controls.Add(TitlePanel);

            TitlePanel.Autosize();
            MonthTable.Autosize();
        }

        void ChangeMonth(int months)
        {
            CurrentDate = CurrentDate.AddMonths(months);
        }

        void DateChanged()
        {
            TitlePanel.SetMonthLabel(CurrentDate.Month - 1, CurrentDate.Year);

            MonthTable.Visible = false;
            MonthTable.SuspendLayout();
            MonthTable.Controls.Clear();
            MonthTable.UpdateCurrentMonth(CurrentDate);
            MonthTable.SetupContents();
            MonthTable.ResumeLayout();
            MonthTable.Visible = true;
        }

        public void AutosizeControl(object? sender, EventArgs e)
        {
            TitlePanel.Autosize();
            MonthTable.Autosize();
        }
    }

    [ToolboxItem(false)]
    public class CustomMonthCalendarHeader : TableLayoutPanel
    {
        string[] monthNames = new CultureInfo("en-US").DateTimeFormat.MonthNames;
        int curViewMonth;
        int curViewYear;

        Button PrevMonthButton;
        Label CurrentMonthLabel;
        Button NextMonthButton;

        public event Action<int> MonthChanged;

        public CustomMonthCalendarHeader(int month, int year)
        {
            curViewMonth = month;
            curViewYear = year;
            SetupStyle();
            SetupContents();
        }

        void SetupStyle()
        {
            CellBorderStyle = TableLayoutPanelCellBorderStyle.Single;
            Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right;
            Dock = DockStyle.Top;
            Size = new Size(Width, Height);
            RowCount = 1;
            ColumnCount = 3;
            GrowStyle = TableLayoutPanelGrowStyle.FixedSize;
            ColumnStyles.Clear();
            for (int i = 0; i < ColumnCount; i++)
            {
                var style = new ColumnStyle();
                style.SizeType = SizeType.Percent;
                if (i % 2 == 0)
                    style.Width = 10;
                else
                    style.Width = 80;

                ColumnStyles.Add(style);
            }
        }

        void SetupContents()
        {
            PrevMonthButton = new Button();
            PrevMonthButton.Text = "<";
            PrevMonthButton.Anchor = AnchorStyles.None;
            PrevMonthButton.Click += PrevMonthButton_Click;

            CurrentMonthLabel = new Label();
            CurrentMonthLabel.Text = monthNames[curViewMonth] + " " + curViewYear.ToString();
            CurrentMonthLabel.AutoSize = false;
            CurrentMonthLabel.TextAlign = ContentAlignment.MiddleCenter;
            CurrentMonthLabel.Dock = DockStyle.Fill;

            NextMonthButton = new Button();
            NextMonthButton.Text = ">";
            NextMonthButton.Anchor = AnchorStyles.None;
            NextMonthButton.Click += NextMonthButton_Click;

            Controls.Add(PrevMonthButton, 0, 0);
            Controls.Add(CurrentMonthLabel, 1, 0);
            Controls.Add(NextMonthButton, 2, 0);
        }

        public void SetMonthLabel(int month, int year)
        {
            CurrentMonthLabel.Text = monthNames[month] + " " + year.ToString();
        }

        private void PrevMonthButton_Click(object? sender, EventArgs e)
        {
            MonthChanged(-1);
        }

        private void NextMonthButton_Click(object? sender, EventArgs e)
        {
            MonthChanged(1);
        }

        public void Autosize()
        {
            Size = new Size(Parent.Width, (int)(Parent.Height * 0.15f));
            for (int i = 0; i < ColumnCount; i++)
            {
                var style = ColumnStyles[i];
                style.SizeType = SizeType.Percent;
                if (i % 2 == 0)
                {
                    style.Width = 10;

                    Control control = GetControlFromPosition(i, 0);
                    int width = GetColumnWidths()[i];
                    int height = GetRowHeights()[0];
                    control.Size = new Size(width / 2, height / 2);
                }
                else
                {
                    style.Width = 80;

                    SizeF extent = TextRenderer.MeasureText(
                        CurrentMonthLabel.Text, CurrentMonthLabel.Font);

                    float hRatio = CurrentMonthLabel.Height / extent.Height;
                    float wRatio = CurrentMonthLabel.Width / extent.Width;
                    float ratio = (hRatio < wRatio) ? hRatio : wRatio;
                    float newSize = CurrentMonthLabel.Font.Size * ratio;
                    CurrentMonthLabel.Font = new Font(CurrentMonthLabel.Font.FontFamily, newSize, CurrentMonthLabel.Font.Style);
                }
            }
        }
    }

    [ToolboxItem(false)]
    public class CustomMonthGrid : TableLayoutPanel
    {
        DateTime FirstDayOfMonth;

        public CustomMonthGrid(DateTime firstDayOfMonth)
        {
            FirstDayOfMonth = firstDayOfMonth;
            CellPaint += PaintCells;

            SetupStyle();
            SetupContents();
        }

        private void PaintCells(object? sender, TableLayoutCellPaintEventArgs e)
        {
            e.Graphics.FillRectangle(Brushes.LightPink, e.CellBounds);
        }

        void SetupStyle()
        {
            CellBorderStyle = TableLayoutPanelCellBorderStyle.Single;
            Anchor = AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            Dock = DockStyle.Fill;
            Size = new Size(Width, Height);
            RowCount = GetRowCount();
            ColumnCount = 7;
            GrowStyle = TableLayoutPanelGrowStyle.FixedSize;
            RowStyles.Clear();
            ColumnStyles.Clear();
            for (int i = 0; i < ColumnCount; i++)
            {
                var cStyle = new ColumnStyle();
                var rStyle = new RowStyle();
                cStyle.SizeType = SizeType.Percent;
                rStyle.SizeType = SizeType.Percent;

                if (i == 0)
                    rStyle.Height = 5;
                else
                    rStyle.Height = 95f / (RowCount - 1);

                cStyle.Width = 100 / 7f;

                ColumnStyles.Add(cStyle);
                RowStyles.Add(rStyle);
            }
        }

        int GetRowCount()
        {
            var daysInMonth = DateTime.DaysInMonth(FirstDayOfMonth.Year, FirstDayOfMonth.Month);
            var remainder = daysInMonth % 7;
            if ((int)FirstDayOfMonth.DayOfWeek + remainder > 6)
                return 7;
            else return 6;
        }

        public void SetupContents()
        {
            for (int i = 0; i < ColumnCount; i++)
            {
                var label = new Label();
                label.Text = ((DayOfWeek)i).ToString();
                label.AutoSize = false;
                label.TextAlign = ContentAlignment.MiddleCenter;
                label.Dock = DockStyle.Fill;

                Controls.Add(label, i, 0);
            }

            SetupDayObjects();
        }

        public void UpdateCurrentMonth(DateTime dateTime)
        {
            FirstDayOfMonth = dateTime;
            RowCount = GetRowCount();
        }

        void SetupDayObjects()
        {
            var totalDays = (RowCount - 1) * ColumnCount;
            int firstDay = (int)FirstDayOfMonth.DayOfWeek;

            DateTime curDateTime = FirstDayOfMonth.AddDays(-firstDay);
            for (int i = 0; i < totalDays; i++)
            {
                var day = new CustomDayObject(curDateTime);
                if (curDateTime.Month != FirstDayOfMonth.Month)
                    day.BackColor = Color.LightGray;
                Controls.Add(day);
                curDateTime = curDateTime.AddDays(1);
            }
        }

        public void Autosize()
        {
            Size = new Size(Parent.Width, (int)(Parent.Height * 0.85f));
            for (int i = 0; i < ColumnCount; i++)
            {
                var cStyle = ColumnStyles[i];
                var rStyle = RowStyles[i];
                cStyle.SizeType = SizeType.Percent;
                rStyle.SizeType = SizeType.Percent;

                if (i == 0)
                    rStyle.Height = 5;
                else
                    rStyle.Height = 95 / 6f;
            }
        }
    }

    [ToolboxItem(false)]
    public class CustomDayObject : TableLayoutPanel
    {
        public DateTime Day;
        int eventCount = 0;
        public List<CalendarEvent> EventList = new List<CalendarEvent>();

        Label eventHeader;
        Label eventDescBox;

        public CustomDayObject(DateTime day)
        {
            Day = day;
            SetupStyle();
            SetupContent();
        }

        void SetupStyle()
        {
            CellBorderStyle = TableLayoutPanelCellBorderStyle.Single;
            Anchor = AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            Dock = DockStyle.Fill;
            Size = new Size(Width, Height);
            RowCount = 2;
            ColumnCount = 2;
            GrowStyle = TableLayoutPanelGrowStyle.FixedSize;
            RowStyles.Clear();
            ColumnStyles.Clear();

            var rStyle1 = new RowStyle();
            rStyle1.SizeType = SizeType.Percent;
            rStyle1.Height = 20;

            var rStyle2 = new RowStyle();
            rStyle2.SizeType = SizeType.Percent;
            rStyle2.Height = 80;

            var cStyle1 = new ColumnStyle();
            cStyle1.SizeType = SizeType.Percent;
            cStyle1.Width = 15;

            var cStyle2 = new ColumnStyle();
            cStyle2.SizeType = SizeType.Percent;
            cStyle2.Width = 85;

            RowStyles.Add(rStyle1);
            RowStyles.Add(rStyle2);
            ColumnStyles.Add(cStyle1);
            ColumnStyles.Add(cStyle2);
        }

        void SetupContent()
        {
            var dayLabel = new Label();
            dayLabel.Dock = DockStyle.Fill;
            dayLabel.AutoSize = false;
            dayLabel.TextAlign = ContentAlignment.MiddleCenter;
            dayLabel.Text = Day.Day.ToString();

            eventHeader = new Label();
            eventHeader.Dock = DockStyle.Fill;
            eventHeader.AutoSize = false;
            eventHeader.TextAlign = ContentAlignment.MiddleRight;
            eventHeader.Text = "No events this day";

            eventDescBox = new Label();
            eventDescBox.Dock = DockStyle.Fill;
            eventDescBox.AutoSize = false;
            eventDescBox.Text = "";
            SetColumnSpan(eventDescBox, 2);
            eventDescBox.Click += onClick;

            SetData();

            Controls.Add(dayLabel, 0, 0);
            Controls.Add(eventHeader, 1, 0);
            Controls.Add(eventDescBox, 0, 1);
        }

        private void onClick(object? sender, EventArgs e)
        {
            EventViewForm form2 = new EventViewForm(this);
            form2.ShowDialog();
        }

        public void SetData()
        {
            EventList = JSONHelper.GetEventsForDay(Day);
            if (EventList == null || EventList.Count == 0)
                return;

            eventCount = EventList.Count;
            eventHeader.Text = $"{eventCount} events this day";

            eventDescBox.Text = "";
            foreach (var _event in EventList)
            {
                eventDescBox.Text += $"{_event.Time[0].ToString("hh':'mm")} -" +
                    $" {_event.Time[1].ToString("hh':'mm")}: {_event.Event}\n";
            }
        }

        public void Autosize()
        {
            RowStyles.Clear();
            ColumnStyles.Clear();

            var rStyle1 = new RowStyle();
            rStyle1.SizeType = SizeType.Percent;
            rStyle1.Height = 20;

            var rStyle2 = new RowStyle();
            rStyle2.SizeType = SizeType.Percent;
            rStyle2.Height = 80;

            var cStyle1 = new ColumnStyle();
            cStyle1.SizeType = SizeType.Percent;
            cStyle1.Width = 15;

            var cStyle2 = new ColumnStyle();
            cStyle2.SizeType = SizeType.Percent;
            cStyle2.Width = 85;

            RowStyles.Add(rStyle1);
            RowStyles.Add(rStyle2);
            ColumnStyles.Add(cStyle1);
            ColumnStyles.Add(cStyle2);
        }
    }

    public class CalendarEvent
    {
        public DateTime Date = DateTime.Now;
        public string Event = "";
        public TimeSpan[] Time = new TimeSpan[2];

        public CalendarEvent(DateTime date, string _event, TimeSpan[] time)
        {
            Date = date;
            Event = _event;
            Time = time;
        }

        public static List<CalendarEvent> FromJson(string json)
        {
            return JsonConvert.DeserializeObject<List<CalendarEvent>>(json)!;
        }

        public string ToJson()
        {
            return JsonConvert.SerializeObject(this);
        }
    }

    public class EventViewForm : Form
    {
        CustomDayObject DayObject;
        Label EventDetails;
        public EventViewForm(CustomDayObject dayObject)
        {
            DayObject = dayObject;
            FormBorderStyle = FormBorderStyle.None;
            Size = new Size((int)(Width * 2.5f), Height * 3);
            StartPosition = FormStartPosition.CenterScreen;

            Panel panel1 = new Panel();
            panel1.Dock = DockStyle.Top;
            panel1.BorderStyle = BorderStyle.FixedSingle;

            Button addEventBtn = new Button();
            addEventBtn.Text = "Add Event";
            addEventBtn.BackColor = Color.LightGreen;
            addEventBtn.Anchor = AnchorStyles.None;
            addEventBtn.Dock = DockStyle.Fill;
            addEventBtn.Click += AddEvent;

            panel1.Controls.Add(addEventBtn);


            Panel panel2 = new Panel();
            panel2.Dock = DockStyle.Fill;

            EventDetails = new Label();
            EventDetails.Dock = DockStyle.Fill;
            EventDetails.AutoSize = false;
            EventDetails.Text = "";
            UpdateEventDetailText();

            panel2.Controls.Add(EventDetails);

            Button okBtn = new Button();
            okBtn.Text = "OK";
            okBtn.Height = 50;
            okBtn.Dock = DockStyle.Bottom;
            okBtn.Click += OkBtn_Click;

            Controls.Add(panel2);
            Controls.Add(okBtn);
            Controls.Add(panel1);
        }

        private void OkBtn_Click(object? sender, EventArgs e)
        {
            DayObject.SetData();
            Close();
        }

        Form promptForm = new Form();
        private void AddEvent(object? sender, EventArgs e)
        {
            promptForm = new Form();
            promptForm.StartPosition = FormStartPosition.CenterScreen;
            promptForm.Size = new Size(Width, Height);

            var lbl1 = new Label();
            lbl1.Text = "Enter a start time";
            lbl1.Location = new Point(10, 10);
            lbl1.Size = new Size(1000, 50);

            var dtp = new DateTimePicker();
            dtp.Format = DateTimePickerFormat.Custom;
            dtp.CustomFormat = "HH':'mm";
            dtp.ShowUpDown = true;
            dtp.Location = new Point(10, 70);

            var lbl2 = new Label();
            lbl2.Text = "Enter an end time";
            lbl2.Location = new Point(10, 130);
            lbl2.Size = new Size(1000, 50);

            var dtp2 = new DateTimePicker();
            dtp2.Format = DateTimePickerFormat.Custom;
            dtp2.CustomFormat = "HH':'mm";
            dtp2.ShowUpDown = true;
            dtp2.Location = new Point(10, 190);

            var lbl3 = new Label();
            lbl3.Text = "Enter a description";
            lbl3.Location = new Point(10, 250);
            lbl3.Size = new Size(1000, 50);

            var tbx = new TextBox();
            tbx.Multiline = true;
            tbx.Location = new Point(10, 310);
            tbx.Size = new Size(500, 250);

            var okayBtn = new Button();
            okayBtn.Text = "OK";
            okayBtn.Location = new Point(250, 570);
            okayBtn.Size = new Size(200, 50);
            okayBtn.Click += (sender, e) => OKClicked(sender, e, new List<string> { dtp.Text, dtp2.Text, tbx.Text });

            promptForm.Controls.Add(lbl1);
            promptForm.Controls.Add(dtp);
            promptForm.Controls.Add(lbl2);
            promptForm.Controls.Add(dtp2);
            promptForm.Controls.Add(lbl3);
            promptForm.Controls.Add(tbx);
            promptForm.Controls.Add(okayBtn);
            promptForm.ShowDialog();
        }

        void OKClicked(object? sender, EventArgs e, List<string> args)
        {
            TimeSpan ts1 = TimeSpan.Parse(args[0]);
            TimeSpan ts2 = TimeSpan.Parse(args[1]);

            bool collision = false;
            foreach (var _event in DayObject.EventList)
            {
                if ((_event.Time[0] > ts1) && (_event.Time[0] < ts2))
                    collision = true;
                if ((_event.Time[1] > ts1) && (_event.Time[1] < ts2))
                    collision = true;
                if (collision)
                {
                    MessageBox.Show($"There is a time collision with the {_event.Event} event.");
                    break;
                }
            }
            if (collision) return;

            var newEvent = new CalendarEvent(DayObject.Day, args[2], new TimeSpan[] { ts1, ts2 });
            JSONHelper.AddEvent(newEvent);
            UpdateEventDetailText();
            promptForm.Close();
        }

        void UpdateEventDetailText()
        {
            if (DayObject.EventList == null || DayObject.EventList.Count == 0)
                return;

            EventDetails.Text = "";
            foreach (var _event in DayObject.EventList)
            {
                EventDetails.Text += $"{_event.Time[0].ToString("hh':'mm")} -" +
                    $" {_event.Time[1].ToString("hh':'mm")}: {_event.Event}\n\n";
            }
        }
    }

    public class JSONHelper
    {
        public static Dictionary<DateTime, List<CalendarEvent>> EventDB = new Dictionary<DateTime, List<CalendarEvent>>();

        public static void Init()
        {
            string json = File.ReadAllText("eventss.json");
            var array = JArray.Parse(json);
            var tokens = array.ToArray();
            foreach (var token in tokens)
            {
                var _event = token.ToObject<CalendarEvent>();
                if (_event == null)
                    continue;
                if (EventDB.ContainsKey(_event.Date))
                    EventDB[_event.Date].Add(_event);
                else
                    EventDB.Add(_event.Date, new List<CalendarEvent>() { _event });
            }
        }

        public static void AddEvent(CalendarEvent calendarEvent)
        {
            if (EventDB.ContainsKey(calendarEvent.Date))
                EventDB[calendarEvent.Date].Add(calendarEvent);
            else
                EventDB.Add(calendarEvent.Date, new List<CalendarEvent>() { calendarEvent });

            List<CalendarEvent> allEvents = new List<CalendarEvent>();
            foreach (var lst in EventDB.Values)
            {
                allEvents = allEvents.Concat(lst).ToList();
            }

            var jArrayString = JArray.FromObject(allEvents).ToString();
            File.WriteAllText("eventss.json", jArrayString);
        }

        public static List<CalendarEvent>? GetEventsForDay(DateTime date)
        {
            if (EventDB.ContainsKey(date))
                return EventDB[date];
            else
                return new List<CalendarEvent>();
        }
    }
}
