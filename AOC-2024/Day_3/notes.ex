# Create sublists from a list
defmodule ListCombinator do
  def sublists(list) do
    Enum.map(0..(length(list) - 1), &(List.delete_at(list, &1)))
  end
end

inputList = [1, 2, 3, 4]
inputList |> IO.inspect(label: "Input")

IO.inspect(ListCombinator.sublists(inputList), label: "Output")


# Remove the first occurence of a value
valToRemove = 1
[[0, 1, 1, 0], [0, 0, 1, 1], [1, 1, 0, 0], [1, 0, 1, 0], [0, 0, 0, 0]]
 |> Enum.map(fn list ->
      r = Enum.split_while(list, &(&1 != valToRemove))
      #IO.inspect(r)
      case r do
        {result, [_ | rest]} -> result ++ rest
        {result, []} -> result
      end
    end)
  |> IO.inspect()


defmodule Advent do
  def doWork(numList, incDir) do
    Enum.chunk_every(numList, 2, 1, :discard)
    |> Enum.map(fn [a, b] ->
        if abs(a - b) in 1..3 do
          if incDir == :dec do
            if(a - b > 0, do: 0, else: 1)
          else
            if(a - b < 0, do: 0, else: 1)
          end
        else
          1
        end
       end)
    |> Enum.sum()
    #|> IO.inspect()

    #IO.puts("")
  end
end

myList = [[7, 6, 4, 2, 1],[1, 2, 7, 8, 9],[9, 7, 6, 2, 1],[1, 3, 2, 4, 5],[8, 6, 4, 4, 1],[1, 3, 6, 7, 9]]

Enum.map(myList, fn numList ->
  if((Enum.at(numList,0) - Enum.at(numList,1)) > 0, do: Advent.doWork(numList, :dec), else: Advent.doWork(numList, :inc))
  end)
  |> IO.inspect()
  #IO.puts("Safe Records: #{safeRecords}")



Enum.map(myList, fn [first, second] = list -> 
  direction = if first - second > 0, do: :dec, else: :inc
  doWork(list, direction)
end)

def doWork(numList, :dec) when is_list(numList) do
  IO.inspect(numList)
end
def doWork(numList, :inc) when is_list(numList) do
  IO.inspect(numList)
end
def doWork([_], :dec), do: 20
