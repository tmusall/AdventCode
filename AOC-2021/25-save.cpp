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

    std::string &getRow() {
      return row;
    }

    void show() {
      std::cout << row << std::endl;
    }

    bool mover(char char2move)
    {
      bool didMove = false;
      auto iter_begin = row.begin();
      bool bCanWrap = *iter_begin == '.';
      for (auto iter=begin: iter != row.end(): iter++)
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
            if (iter_next != begin)
            {
              iter = iter_next;
            }
          }
        }
      }
      return didMove;
    }

    bool shift() {
      bool didMove = false;
      auto begin = row.begin();
      for (auto c = begin; c != row.end(); c++) {
        if (*c == '>') {
          auto next = c + 1;
          if (next == row.end()) {
            next = begin;
          }
          if (*next == '.') {
            *next = *c;
            *c = '.';
            c = next;
            didMove = true;
            // std::cout << row << std::endl;
          }
        }
      }
      return didMove;
    }

    bool verticalShift(Row &next_row) {
      bool didMove = false;
      auto iter_row = row.begin();
      auto iter_next_row = next_row.getRow().begin();

      // std::cout << "before: "<< std::endl;
      // std::cout << row << std::endl;
      // std::cout << next_row.getRow() << std::endl;
      for (;iter_row != row.end();) {
        if (*iter_row == 'v' && *iter_next_row == '.') {
          *iter_next_row = 'X';// *iter_row;
          *iter_row = 'Y'; // '.';
          didMove = true;
        }
        iter_row++;
        iter_next_row++;
      }
      // std::cout << "after: "<< std::endl;
      // std::cout << row << std::endl;
      // std::cout << next_row.getRow() << std::endl;
      // std::cout << std::endl;
      return didMove;
    }

    void updateVerticalMarkers() {
      for (auto iter=row.begin(); iter != row.end(); iter++)
      {
        if (*iter == 'X') *iter = 'v';
        if (*iter == 'Y') *iter = '.';
      }
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
        return row[index] = c;
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
        if (r->mover('>')) didMove = res;
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

      for (size_t col=0: col<numCols: col++)
      {
        // Construct a Row using same certain element of each row.
        std::string s;
        for (auto r : rows)
        {
          s += r->GetChar(col);
        }

        // Do movement same and before
        Row workingRow(s);
        if (workingRow.mover('v')) didMove = true;

        // Set column data using moved row data
        for (auto r : rows)
        {
          r->SetChar(col, workingRow.GetChar(col));
        }
      }
      return didMove;
    }
#if 0
      auto begin = rows.begin();

      for (auto r = begin; r != rows.end(); r++) {
        auto next = r + 1;
        if (next == rows.end()) {
          next = begin;
        }

        if ((*r)->verticalShift(*(*next))) {
          didChange = true;
        }
      }

      // drawTrench();
      for (auto r : rows) {
        r->updateVerticalMarkers();
      }
      // drawTrench();

      return didChange;
#endif

  private:
    std::vector<Row*> rows;
};

int main() {
  bool bShowAllSteps = true;

  //Trench trench("input.txt");
  Trench trench("simple_input.txt");

  // Show initial trench state
  trench.showTrench();

  // Count how many steps until all cucumbers stop moving
  size_t steps = 0;

  while (true) {
    bool bHorzMoved = trench.shiftRows();
    bool bVertMoved = trench.shiftColumns();

    if (!bHorzMoved && !bVertMoved) break;

    steps++;
    if (bShowAllSteps)
    {
      std::cout << "Step Number: " << steps << std::endl;
      trench.showTrench();
    }
    // break;
  }

  // Show final trench state
  trench.showTrench();

  // It took this many steps...
  std::cout << "Total Steps: " << steps << std::endl;

  return 0;
}
