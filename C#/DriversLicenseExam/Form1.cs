using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace DriversLicenseExam
{
    public partial class Form1 : Form
    {
        string[] FirstSetCorrectAnswers = new string[] { "B", "D", "A", "A",
            "C", "A", "B", "C", "A", "D", "B", "C", "D",
            "A", "D", "C", "C", "B", "D", "A" };

        string[] CorrectAnswers = new string[20];
        string[] StudentAnswers = new string[20];

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            CorrectAnswers = FirstSetCorrectAnswers;
            GradeExam();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();
            openFileDialog.Filter = "txt files (*.txt)|*.txt";
            openFileDialog.InitialDirectory = Directory.GetCurrentDirectory();
            if (openFileDialog.ShowDialog() != DialogResult.OK)
                return;
            CorrectAnswers = LoadAnswers(openFileDialog.FileName);

            GradeExam();
        }

        void GradeExam()
        {
            StudentAnswers = LoadAnswers("StudentAnswers.txt");
            ExamReport report = GenerateGradedReport();
            ShowReport(report);
        }

        void ShowReport(ExamReport report)
        {
            label5.Text = report.Passed ? "Pass" : "Fail";
            label6.Text = report.CorrectAnswers.ToString();
            label7.Text = report.IncorrectAnswers.ToString();
            label8.Text = string.Join("; ", report.IncorrectAnswerQuestionNumbers);
        }

        string[] LoadAnswers(string filename)
        {
            return File.ReadAllLines(filename);
        }

        ExamReport GenerateGradedReport()
        {
            ExamReport report = new ExamReport();
            report.CorrectAnswers = 0;
            report.IncorrectAnswers = 0;
            report.Passed = false;
            report.IncorrectAnswerQuestionNumbers = new List<int>();
            for (int i = 0; i < CorrectAnswers.Length; i++)
            {
                if (StudentAnswers[i] == CorrectAnswers[i])
                    report.CorrectAnswers++;
                else
                {
                    report.IncorrectAnswers++;
                    report.IncorrectAnswerQuestionNumbers.Add(i + 1);
                }
            }
            report.Passed = report.CorrectAnswers >= 15;
            return report;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            // Save Grade
            ExamRecord record = new ExamRecord();
            record.Name = "Student";
            record.AnswersGiven = StudentAnswers;
            record.Passed = (label5.Text == "Pass") ? true : false;
            record.ExamDate = DateTime.Today.Date;

            SaveRecord(record);
        }

        void SaveRecord(ExamRecord record)
        {
            List<string> lines = new List<string>
            {
                "\n",
                "Name: " + record.Name,
                "Answers: " + string.Join("; ", record.AnswersGiven),
                "Pass: " + record.Passed.ToString(),
                "ExamDate: " + record.ExamDate.ToString(),
                "\n"
            };

            File.AppendAllLines("ExamRecords.txt", lines);
        }
    }

    public struct ExamRecord
    {
        public string Name;
        public string[] AnswersGiven;
        public bool Passed;
        public DateTime ExamDate;
    }

    public struct ExamReport
    {
        public bool Passed;
        public int CorrectAnswers;
        public int IncorrectAnswers;
        public List<int> IncorrectAnswerQuestionNumbers;
    }
}