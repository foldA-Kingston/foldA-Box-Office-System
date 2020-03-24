import { format } from "date-fns";

export const formatDate = date => format(new Date(date), "h:mma E. MMMM d");
