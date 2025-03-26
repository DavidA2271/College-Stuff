namespace CIS302FinalExam
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            button1 = new Button();
            button2 = new Button();
            tableLayoutPanel1 = new TableLayoutPanel();
            discountLabel = new Label();
            label14 = new Label();
            pTotalLabel = new Label();
            label12 = new Label();
            mailingLabel = new Label();
            label10 = new Label();
            customeridLabel = new Label();
            label8 = new Label();
            phnLabel = new Label();
            label6 = new Label();
            addressLabel = new Label();
            label4 = new Label();
            nameLabel = new Label();
            label2 = new Label();
            label1 = new Label();
            tableLayoutPanel1.SuspendLayout();
            SuspendLayout();
            // 
            // button1
            // 
            button1.Location = new Point(268, 265);
            button1.Name = "button1";
            button1.Size = new Size(131, 40);
            button1.TabIndex = 0;
            button1.Text = "Back";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // button2
            // 
            button2.Location = new Point(1113, 260);
            button2.Name = "button2";
            button2.Size = new Size(131, 40);
            button2.TabIndex = 1;
            button2.Text = "Next";
            button2.UseVisualStyleBackColor = true;
            button2.Click += button2_Click;
            // 
            // tableLayoutPanel1
            // 
            tableLayoutPanel1.CellBorderStyle = TableLayoutPanelCellBorderStyle.InsetDouble;
            tableLayoutPanel1.ColumnCount = 2;
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50F));
            tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50F));
            tableLayoutPanel1.Controls.Add(discountLabel, 1, 6);
            tableLayoutPanel1.Controls.Add(label14, 0, 6);
            tableLayoutPanel1.Controls.Add(pTotalLabel, 1, 5);
            tableLayoutPanel1.Controls.Add(label12, 0, 5);
            tableLayoutPanel1.Controls.Add(mailingLabel, 1, 4);
            tableLayoutPanel1.Controls.Add(label10, 0, 4);
            tableLayoutPanel1.Controls.Add(customeridLabel, 1, 3);
            tableLayoutPanel1.Controls.Add(label8, 0, 3);
            tableLayoutPanel1.Controls.Add(phnLabel, 1, 2);
            tableLayoutPanel1.Controls.Add(label6, 0, 2);
            tableLayoutPanel1.Controls.Add(addressLabel, 1, 1);
            tableLayoutPanel1.Controls.Add(label4, 0, 1);
            tableLayoutPanel1.Controls.Add(nameLabel, 1, 0);
            tableLayoutPanel1.Controls.Add(label2, 0, 0);
            tableLayoutPanel1.Location = new Point(497, 87);
            tableLayoutPanel1.Name = "tableLayoutPanel1";
            tableLayoutPanel1.RowCount = 7;
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 14.2857141F));
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 14.2857141F));
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 14.2857141F));
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 14.2857141F));
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 14.2857141F));
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 14.2857141F));
            tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 14.2857141F));
            tableLayoutPanel1.Size = new Size(447, 461);
            tableLayoutPanel1.TabIndex = 2;
            // 
            // discountLabel
            // 
            discountLabel.Anchor = AnchorStyles.None;
            discountLabel.AutoSize = true;
            discountLabel.Location = new Point(295, 410);
            discountLabel.Name = "discountLabel";
            discountLabel.Size = new Size(79, 30);
            discountLabel.TabIndex = 13;
            discountLabel.Text = "label15";
            discountLabel.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // label14
            // 
            label14.Anchor = AnchorStyles.None;
            label14.AutoSize = true;
            label14.Location = new Point(65, 410);
            label14.Name = "label14";
            label14.Size = new Size(95, 30);
            label14.TabIndex = 12;
            label14.Text = "Discount";
            label14.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // pTotalLabel
            // 
            pTotalLabel.Anchor = AnchorStyles.None;
            pTotalLabel.AutoSize = true;
            pTotalLabel.Location = new Point(295, 344);
            pTotalLabel.Name = "pTotalLabel";
            pTotalLabel.Size = new Size(79, 30);
            pTotalLabel.TabIndex = 11;
            pTotalLabel.Text = "label13";
            pTotalLabel.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // label12
            // 
            label12.Anchor = AnchorStyles.None;
            label12.AutoSize = true;
            label12.Location = new Point(39, 344);
            label12.Name = "label12";
            label12.Size = new Size(147, 30);
            label12.TabIndex = 10;
            label12.Text = "Purchase Total";
            label12.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // mailingLabel
            // 
            mailingLabel.Anchor = AnchorStyles.None;
            mailingLabel.AutoSize = true;
            mailingLabel.Location = new Point(295, 279);
            mailingLabel.Name = "mailingLabel";
            mailingLabel.Size = new Size(79, 30);
            mailingLabel.TabIndex = 9;
            mailingLabel.Text = "label11";
            mailingLabel.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // label10
            // 
            label10.Anchor = AnchorStyles.None;
            label10.AutoSize = true;
            label10.Location = new Point(53, 279);
            label10.Name = "label10";
            label10.Size = new Size(119, 30);
            label10.TabIndex = 8;
            label10.Text = "Mailing List";
            label10.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // customeridLabel
            // 
            customeridLabel.Anchor = AnchorStyles.None;
            customeridLabel.AutoSize = true;
            customeridLabel.Location = new Point(300, 214);
            customeridLabel.Name = "customeridLabel";
            customeridLabel.Size = new Size(68, 30);
            customeridLabel.TabIndex = 7;
            customeridLabel.Text = "label9";
            customeridLabel.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // label8
            // 
            label8.Anchor = AnchorStyles.None;
            label8.AutoSize = true;
            label8.Location = new Point(51, 214);
            label8.Name = "label8";
            label8.Size = new Size(123, 30);
            label8.TabIndex = 6;
            label8.Text = "CustomerID";
            label8.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // phnLabel
            // 
            phnLabel.Anchor = AnchorStyles.None;
            phnLabel.AutoSize = true;
            phnLabel.Location = new Point(300, 149);
            phnLabel.Name = "phnLabel";
            phnLabel.Size = new Size(68, 30);
            phnLabel.TabIndex = 5;
            phnLabel.Text = "label7";
            phnLabel.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // label6
            // 
            label6.Anchor = AnchorStyles.None;
            label6.AutoSize = true;
            label6.Location = new Point(76, 149);
            label6.Name = "label6";
            label6.Size = new Size(72, 30);
            label6.TabIndex = 4;
            label6.Text = "Phone";
            label6.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // addressLabel
            // 
            addressLabel.Anchor = AnchorStyles.None;
            addressLabel.AutoSize = true;
            addressLabel.Location = new Point(300, 84);
            addressLabel.Name = "addressLabel";
            addressLabel.Size = new Size(68, 30);
            addressLabel.TabIndex = 3;
            addressLabel.Text = "label5";
            addressLabel.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // label4
            // 
            label4.Anchor = AnchorStyles.None;
            label4.AutoSize = true;
            label4.Location = new Point(69, 84);
            label4.Name = "label4";
            label4.Size = new Size(87, 30);
            label4.TabIndex = 2;
            label4.Text = "Address";
            label4.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // nameLabel
            // 
            nameLabel.Anchor = AnchorStyles.None;
            nameLabel.AutoSize = true;
            nameLabel.Location = new Point(300, 19);
            nameLabel.Name = "nameLabel";
            nameLabel.Size = new Size(68, 30);
            nameLabel.TabIndex = 1;
            nameLabel.Text = "label3";
            nameLabel.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // label2
            // 
            label2.Anchor = AnchorStyles.None;
            label2.AutoSize = true;
            label2.Location = new Point(78, 19);
            label2.Name = "label2";
            label2.Size = new Size(69, 30);
            label2.TabIndex = 0;
            label2.Text = "Name";
            label2.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(661, 27);
            label1.Name = "label1";
            label1.Size = new Size(102, 30);
            label1.TabIndex = 3;
            label1.Text = "Customer";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(12F, 30F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(1417, 610);
            Controls.Add(label1);
            Controls.Add(tableLayoutPanel1);
            Controls.Add(button2);
            Controls.Add(button1);
            Name = "Form1";
            Text = "Customers";
            tableLayoutPanel1.ResumeLayout(false);
            tableLayoutPanel1.PerformLayout();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button button1;
        private Button button2;
        private TableLayoutPanel tableLayoutPanel1;
        private Label discountLabel;
        private Label label14;
        private Label pTotalLabel;
        private Label label12;
        private Label mailingLabel;
        private Label label10;
        private Label customeridLabel;
        private Label label8;
        private Label phnLabel;
        private Label label6;
        private Label addressLabel;
        private Label label4;
        private Label nameLabel;
        private Label label2;
        private Label label1;
    }
}