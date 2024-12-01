defmodule Main do
  def solve(mode \\ nil) do
    "sample-input.txt"
    |> File.read!()
    |> String.split("\n", trim: true)
    |> parse_groups()
    |> process_groups()
  end

  defp parse_groups(contents) do
    Enum.map(contents, fn line ->
      [left, right] = String.split(line)
      {String.to_integer(left), String.to_integer(right)}
    end)
  end

  defp process_groups(groups) do
    {left, right} = Enum.unzip(groups)

    {
      calc_total_distance(left, right),
      calc_similarity_score(left, right)
    }
  end

  defp calc_total_distance(left, right) do
    Enum.zip(Enum.sort(left), Enum.sort(right))
    |> Enum.map(fn {l, r} -> abs(l - r) end)
    |> Enum.sum()

    res
  end

  defp calc_similarity_score(left, right) do
    right_counts = right |> Enum.frequencies()

    Enum.reduce(left, 0, fn location_id, acc ->
      acc + location_id * Map.get(right_counts, location_id, 0)
    end)
  end
end
