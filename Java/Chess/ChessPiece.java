
public class ChessPiece {
    public int column;
    public int row;
    public Color color;
    public Rank rank;
    //String imgName;

    public ChessPiece(int col, int row, Color color, Rank rank /*String imgName*/) {
        super();
        this.column = col;
        this.row = row;
        this.color = color;
        this.rank = rank;
        //this.imgName = imgName;
    }
}

enum Color
{
    BLACK,
    WHITE
}

enum Rank
{
    PAWN,
    ROOK,
    BISHOP,
    KNIGHT,
    QUEEN,
    KING
}
