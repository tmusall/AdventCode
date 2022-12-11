#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>


class Row {
  public:
    Row(std::string data) {
      row = data;
      length = data.length();
    }

    void show() {
      std::cout << row << std::endl;
    }

    bool mover(char char2move)
    {
      bool didMove = false;
      auto iter_begin = row.begin();
      bool bCanWrap = *iter_begin == '.';

      // std::cout << std::endl << "MoveChar:" << char2move << std::endl;
      // std::cout << "CanWrap:" << bCanWrap << std::endl;
      // std::cout << "Initial:" << std::endl;
      // show();

      for (auto iter=iter_begin; iter != row.end(); iter++)
      {
        if (*iter == char2move)
        {
          auto iter_next = iter + 1;
          // Consider case where we're wrapping back to beginning
          if (iter_next == row.end())
          {
            // Original first char was a '.'
            if (bCanWrap)
            {
              iter_next = iter_begin;
            }
            else
            { // At the end and unable to wrap, so we outta here
              break;
            }
          }

          // Safe to move. This will also wrap if conditions are met.
          if (*iter_next == '.')
          {
            *iter_next = *iter;
            *iter = '.';
            didMove = true;
            // We didn't do a wrap move so advance iter by 2 ...
            //   Once here and again in for() loop
            if (iter_next != iter_begin)
            {
              iter = iter_next;
            }
          }
        }
      }
      // std::cout << "Result:" << std::endl;
      // show();
      return didMove;
    }

    size_t GetLength()
    {
      return length;
    }

    char GetChar(size_t index)
    {
      if (index < length)
      {
        return row.at(index);
      }
      return ' ';
    }

    void SetChar(size_t index, char c)
    {
      if (index < length)
      {
        row[index] = c;
      }
    }

  private:
    std::string row;
    size_t length;
};


class Trench {
  public:
    Trench(std::string file) {
      std::string myText;
      std::ifstream MyReadFile(file);

      while (std::getline(MyReadFile, myText)) {
        rows.push_back(new Row(myText));
      }
    }

    void showTrench() {
      for (auto r : rows) {
        r->show();
      }
      std::cout << std::endl;
    }

    bool shiftRows() {
      bool didMove = false;
      for (auto r : rows) {
        // Simple case, just move each row
        if (r->mover('>')) didMove = true;
      }
      return didMove;
    }

    bool shiftColumns() {
      bool didMove = false;
      // Construct a Row object from vertical column
      // Then use existing Row::mover() to do motion
      // Then map moved row back to vertical column. Easy peasy.

      // Get length of first row. We need to know how many columns
      // we're dealing with here. All rows have same length by def.
      size_t numCols = rows[0]->GetLength();

      for (size_t col=0; col<numCols; col++)
      {
        // Construct a Row using same certain element of each row.
        std::string s;
        for (auto r : rows)
        {
          s += r->GetChar(col);
        }

        // Do movement same as before. Follows all same move rules.
        Row workingRow(s);
        if (workingRow.mover('v')) didMove = true;

        // Set column data using moved row data
        size_t workingIndex = 0;
        for (auto r : rows)
        {
          r->SetChar(col, workingRow.GetChar(workingIndex++));
        }
      }
      return didMove;
    }

  private:
    std::vector<Row*> rows;
};

int main() {
  bool bShowAllSteps = false;

  Trench trench("input.txt");
  //Trench trench("simple_input.txt");

  // Show initial trench state
  std::cout << std::endl << "Initial trench..." << std::endl;
  trench.showTrench();

  // Count how many steps until all cucumbers stop moving
  size_t steps = 1;

  while (true) {
    bool bHorzMoved = trench.shiftRows();
    // std::cout << "After Horz Moves:" << std::endl;
    // trench.showTrench();
    bool bVertMoved = trench.shiftColumns();
    // std::cout << "After Vert Moves:" << std::endl;
    // trench.showTrench();

    if (!bHorzMoved && !bVertMoved) break;

    if (bShowAllSteps)
    {
      std::cout << "Step Number: " << steps << std::endl;
      trench.showTrench();
    }
    steps++;
    if (steps == 1000) break;  // Infinite loop catcher
  }

  // Show final trench state
  std::cout << "Final trench..." << std::endl;
  trench.showTrench();

  // It took this many steps...
  std::cout << "Total Steps: " << steps << std::endl;

  return 0;
}
