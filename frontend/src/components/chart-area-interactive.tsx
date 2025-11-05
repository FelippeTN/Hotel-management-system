"use client"

import * as React from "react"
import { Area, AreaChart, CartesianGrid, XAxis } from "recharts"

import { useIsMobile } from "@/hooks/use-mobile"
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import {
  type ChartConfig,
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
} from "@/components/ui/chart"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"
import {
  ToggleGroup,
  ToggleGroupItem,
} from "@/components/ui/toggle-group"

export const description = "An interactive area chart"

const chartData = [
  { date: "2024-09-01", reservas: 45, receita: 8500 },
  { date: "2024-09-02", reservas: 52, receita: 9200 },
  { date: "2024-09-03", reservas: 48, receita: 8800 },
  { date: "2024-09-04", reservas: 61, receita: 11400 },
  { date: "2024-09-05", reservas: 55, receita: 10200 },
  { date: "2024-09-06", reservas: 67, receita: 12800 },
  { date: "2024-09-07", reservas: 72, receita: 13500 },
  { date: "2024-09-08", reservas: 58, receita: 10800 },
  { date: "2024-09-09", reservas: 49, receita: 9100 },
  { date: "2024-09-10", reservas: 53, receita: 9800 },
  { date: "2024-09-11", reservas: 62, receita: 11600 },
  { date: "2024-09-12", reservas: 68, receita: 12400 },
  { date: "2024-09-13", reservas: 74, receita: 13900 },
  { date: "2024-09-14", reservas: 79, receita: 14800 },
  { date: "2024-09-15", reservas: 65, receita: 12100 },
  { date: "2024-09-16", reservas: 56, receita: 10400 },
  { date: "2024-09-17", reservas: 51, receita: 9500 },
  { date: "2024-09-18", reservas: 59, receita: 11000 },
  { date: "2024-09-19", reservas: 66, receita: 12300 },
  { date: "2024-09-20", reservas: 71, receita: 13300 },
  { date: "2024-09-21", reservas: 76, receita: 14200 },
  { date: "2024-09-22", reservas: 82, receita: 15400 },
  { date: "2024-09-23", reservas: 69, receita: 12900 },
  { date: "2024-09-24", reservas: 60, receita: 11200 },
  { date: "2024-09-25", reservas: 54, receita: 10100 },
  { date: "2024-09-26", reservas: 63, receita: 11800 },
  { date: "2024-09-27", reservas: 70, receita: 13100 },
  { date: "2024-09-28", reservas: 77, receita: 14400 },
  { date: "2024-09-29", reservas: 84, receita: 15800 },
  { date: "2024-09-30", reservas: 88, receita: 16500 },
  { date: "2024-10-01", reservas: 73, receita: 13700 },
  { date: "2024-10-02", reservas: 64, receita: 12000 },
  { date: "2024-10-03", reservas: 57, receita: 10600 },
  { date: "2024-10-04", reservas: 68, receita: 12700 },
  { date: "2024-10-05", reservas: 75, receita: 14000 },
  { date: "2024-10-06", reservas: 81, receita: 15200 },
  { date: "2024-10-07", reservas: 86, receita: 16100 },
  { date: "2024-10-08", reservas: 91, receita: 17100 },
  { date: "2024-10-09", reservas: 78, receita: 14600 },
  { date: "2024-10-10", reservas: 69, receita: 12900 },
  { date: "2024-10-11", reservas: 62, receita: 11600 },
  { date: "2024-10-12", reservas: 71, receita: 13300 },
  { date: "2024-10-13", reservas: 79, receita: 14800 },
  { date: "2024-10-14", reservas: 85, receita: 15900 },
  { date: "2024-10-15", reservas: 90, receita: 16900 },
  { date: "2024-10-16", reservas: 95, receita: 17800 },
  { date: "2024-10-17", reservas: 82, receita: 15400 },
  { date: "2024-10-18", reservas: 74, receita: 13900 },
  { date: "2024-10-19", reservas: 67, receita: 12500 },
  { date: "2024-10-20", reservas: 76, receita: 14200 },
  { date: "2024-10-21", reservas: 83, receita: 15600 },
  { date: "2024-10-22", reservas: 89, receita: 16700 },
  { date: "2024-10-23", reservas: 94, receita: 17600 },
  { date: "2024-10-24", reservas: 99, receita: 18600 },
  { date: "2024-10-25", reservas: 87, receita: 16300 },
  { date: "2024-10-26", reservas: 79, receita: 14800 },
  { date: "2024-10-27", reservas: 72, receita: 13500 },
  { date: "2024-10-28", reservas: 81, receita: 15200 },
  { date: "2024-10-29", reservas: 88, receita: 16500 },
  { date: "2024-10-30", reservas: 93, receita: 17400 },
  { date: "2024-10-31", reservas: 97, receita: 18200 },
  { date: "2024-11-01", reservas: 102, receita: 19100 },
  { date: "2024-11-02", reservas: 91, receita: 17100 },
  { date: "2024-11-03", reservas: 84, receita: 15800 },
  { date: "2024-11-04", reservas: 89, receita: 16700 },
]

const chartConfig = {
  reservas: {
    label: "Reservas",
    color: "hsl(var(--chart-1))",
  },
  receita: {
    label: "Receita (x100 R$)",
    color: "hsl(var(--chart-2))",
  },
} satisfies ChartConfig

export function ChartAreaInteractive() {
  const isMobile = useIsMobile()
  const [timeRange, setTimeRange] = React.useState("90d")

  React.useEffect(() => {
    if (isMobile) {
      setTimeRange("7d")
    }
  }, [isMobile])

  const filteredData = chartData.filter((item) => {
    const date = new Date(item.date)
    const referenceDate = new Date("2024-06-30")
    let daysToSubtract = 90
    if (timeRange === "30d") {
      daysToSubtract = 30
    } else if (timeRange === "7d") {
      daysToSubtract = 7
    }
    const startDate = new Date(referenceDate)
    startDate.setDate(startDate.getDate() - daysToSubtract)
    return date >= startDate
  })

  return (
    <Card className="@container/card">
      <CardHeader>
        <CardTitle>Desempenho do Hotel</CardTitle>
        <CardDescription>
          <span className="hidden @[540px]/card:block">
            Reservas e receita dos últimos 2 meses
          </span>
          <span className="@[540px]/card:hidden">Últimos 2 meses</span>
        </CardDescription>
        <CardAction>
          <ToggleGroup
            type="single"
            value={timeRange}
            onValueChange={setTimeRange}
            variant="outline"
            className="hidden *:data-[slot=toggle-group-item]:!px-4 @[767px]/card:flex"
          >
            <ToggleGroupItem value="90d">Últimos 2 meses</ToggleGroupItem>
            <ToggleGroupItem value="30d">Últimos 30 dias</ToggleGroupItem>
            <ToggleGroupItem value="7d">Últimos 7 dias</ToggleGroupItem>
          </ToggleGroup>
          <Select value={timeRange} onValueChange={setTimeRange}>
            <SelectTrigger
              className="flex w-40 **:data-[slot=select-value]:block **:data-[slot=select-value]:truncate @[767px]/card:hidden"
              size="sm"
              aria-label="Selecione um período"
            >
              <SelectValue placeholder="Últimos 2 meses" />
            </SelectTrigger>
            <SelectContent className="rounded-xl">
              <SelectItem value="90d" className="rounded-lg">
                Últimos 2 meses
              </SelectItem>
              <SelectItem value="30d" className="rounded-lg">
                Últimos 30 dias
              </SelectItem>
              <SelectItem value="7d" className="rounded-lg">
                Últimos 7 dias
              </SelectItem>
            </SelectContent>
          </Select>
        </CardAction>
      </CardHeader>
      <CardContent className="px-2 pt-4 sm:px-6 sm:pt-6">
        <ChartContainer
          config={chartConfig}
          className="aspect-auto h-[250px] w-full"
        >
          <AreaChart data={filteredData}>
            <defs>
              <linearGradient id="fillDesktop" x1="0" y1="0" x2="0" y2="1">
                <stop
                  offset="5%"
                  stopColor="var(--color-desktop)"
                  stopOpacity={1.0}
                />
                <stop
                  offset="95%"
                  stopColor="var(--color-desktop)"
                  stopOpacity={0.1}
                />
              </linearGradient>
              <linearGradient id="fillMobile" x1="0" y1="0" x2="0" y2="1">
                <stop
                  offset="5%"
                  stopColor="var(--color-mobile)"
                  stopOpacity={0.8}
                />
                <stop
                  offset="95%"
                  stopColor="var(--color-mobile)"
                  stopOpacity={0.1}
                />
              </linearGradient>
            </defs>
            <CartesianGrid vertical={false} />
            <XAxis
              dataKey="date"
              tickLine={false}
              axisLine={false}
              tickMargin={8}
              minTickGap={32}
              tickFormatter={(value) => {
                const date = new Date(value)
                return date.toLocaleDateString("en-US", {
                  month: "short",
                  day: "numeric",
                })
              }}
            />
            <ChartTooltip
              cursor={false}
              content={
                <ChartTooltipContent
                  labelFormatter={(value) => {
                    return new Date(value).toLocaleDateString("en-US", {
                      month: "short",
                      day: "numeric",
                    })
                  }}
                  indicator="dot"
                />
              }
            />
            <Area
              dataKey="mobile"
              type="natural"
              fill="url(#fillMobile)"
              stroke="var(--color-mobile)"
              stackId="a"
            />
            <Area
              dataKey="desktop"
              type="natural"
              fill="url(#fillDesktop)"
              stroke="var(--color-desktop)"
              stackId="a"
            />
          </AreaChart>
        </ChartContainer>
      </CardContent>
    </Card>
  )
}
